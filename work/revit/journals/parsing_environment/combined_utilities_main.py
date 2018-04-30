#definitions
def cycle_journal_files(directory_in_str):
	#appends all journal files in folder to list journal_files.
	import os
	
	journal_files = []
	directory = os.fsencode(directory_in_str)
	for file in os.listdir(directory):
		filename = os.fsdecode(file)
		if filename.endswith(".txt") and "dump" not in filename:
			journal_files.append(filename)
			continue
		else:
			continue
	return sorted(journal_files)


def extract_info_project_name_location(filename):
	#parse a journal for file location and project name.
	import codecs
	
	#Variables to store journal info to.
	journal = ""
	path_list = []
	
	#transform journal into parsable string
	with codecs.open(filename, 'r', encoding='utf-8', errors='ignore') as file_object:
		lines = file_object.readlines()
		for line in lines:
			journal = journal + line		
	journal = journal.splitlines()
	
	#Extract the lines that reference ram in the journal.
	for line in journal:
		if "central=" in line.lower() and "slog" in line.lower():
			data = line.split('"<')[0]
			path_list.append([data.splitlines()][0])
			
	#create returnable variables
	file_path = str(path_list[0])[27:]
	file_path = str(file_path.rstrip().strip()[:-4])
	
	project_name = file_path.split("\\")
	for item in project_name:
		if ".rvt" in item:
			project_name = item.strip().rstrip()
			project_name = project_name.split('"')
			project_name = str(project_name[0][:-4])
		else:
			project_name = "error"
	
	return file_path, project_name


def extract_info_date_time(filename):
	#Extracts the date the journal file was opened and closed.
	#import module
	from datetime import datetime
	import codecs
	
	#create list for lines to be stored in.
	start_end = []
	
	#search journals for lines containing "recording journal files"
	try:
		with codecs.open(filename, 'r', encoding='utf-8', errors='ignore') as file_object:
			lines = file_object.readlines()

		for i, line in enumerate(lines):
			if "recording journal file" in line.lower():
				start_end.append(line.strip().lower())
		
	except:
		print("***Could not gather DATE/TIME info from", filename, "***")
	
	#DATES
	#Split lines for dates
	start_date = start_end[0].split(';')[0][3:15].rstrip().strip()
	
	try:
		end_date = start_end[1].split(';')[0][3:15].rstrip().strip()
	
	except:
		end_date = "error"
		
	#TIMES	
	try:	
		#Split lines for times
		start_time = start_end[0].split(';')[0][15:23].rstrip().strip()
		end_time = start_end[1].split(';')[0][15:23].rstrip().strip()
		
		#convert times into datetime objects.
		start_time = datetime.strptime(start_time, '%H:%M:%S')
		end_time = datetime.strptime(end_time, '%H:%M:%S')
			
		#Subtract start and end times for total time.
		tdelta = end_time - start_time

		#Convert datetime objects into readable formats.
		start_time = start_time.strftime('%H:%M:%S %p') #replace H w/ I for 24 hour time
		end_time = end_time.strftime('%H:%M:%S %p') #replace H w/ I for 24 hour time
		tdelta = str(tdelta)
	
	except:
		start_time = start_end[0].split(';')[0][16:23].rstrip().strip()
		end_time = "error"
		tdelta = "error"
		
	return start_date, end_date, start_time, end_time, tdelta


def extract_info_cpu(filename):
	#parses journal for cpu information.
	import re
	import codecs
	
	cpu_info = ""
	
	try:
		with codecs.open(filename, 'r', encoding='utf-8', errors='ignore') as file_object:
			lines = file_object.readlines()

		for i, line in enumerate(lines):
			if re.search(r"processor information:", line.lower()):
				for item in lines[max(i-0, 0):i+19]:
					if "name" in item.lower() or "maxclockspeed" in item.lower() and item not in cpu_info:
						cpu_info = cpu_info + item
					else:
						continue
						
		cpu_info = cpu_info.splitlines()
		
		for item in cpu_info:
			if "name" in item.lower():
				cpu_name = item
				cpu_name = cpu_name.split(":",2)[2].strip()

		for item in cpu_info:
			if "maxclockspeed" in item.lower():
				cpu_clockspeed = item
				cpu_clockspeed = cpu_clockspeed.split(":",2)[2].strip()
				cpu_clockspeed = int(cpu_clockspeed) / 1000
				
		return cpu_name, cpu_clockspeed
		
	except:
		print("***Could not gather CPU info from", filename, "***")


def extract_info_os(filename):
	#parses journal for os information.
	import re
	import codecs
	
	os_info = ""
	
	try:
		with codecs.open(filename, 'r', encoding='utf-8', errors='ignore') as file_object:
			lines = file_object.readlines()

		for i, line in enumerate(lines):
			if re.search(r"operating system info", line.lower()):
				for item in lines[max(i-0, 0):i+20]:
					os_info = os_info + item
		#get os_version       
		os_version = os_info.splitlines()[3]
		os_version = os_version.split(":",2)[2].strip()

		#get os_build
		os_build = os_info.splitlines()[1]
		os_build = os_build.split(":",2)[2].strip()
		
		#return values
		return os_version, os_build

	except:
		print("***Could not gather OS info from", filename, "***")
		
		
def extract_info_graphics(filename):
	#parses journal for graphics hardware info.
	import re
	import codecs
	
	graphics_hardware = {}
	
	try:
		with codecs.open(filename, 'r', encoding='utf-8', errors='ignore') as file_object:
			file_object = file_object.read()
			file_object = file_object.lower().splitlines()
			for line in file_object:
				if "video card environment" in line:
					values = re.findall('"([^"]*)"', line)
					graphics_hardware["gpu_name"] = values[0]
					graphics_hardware["gpu_manufacturer_id"] = values[1]
					graphics_hardware["gpu_device_id"] = values[2]
			return graphics_hardware
			
	except:
		print("***Could not gather GPU info from", filename, "***")


def extract_info_revit(filename):
	#parses journal for Revit info.
	import re
	import codecs
	
	revit_info = ""
	
	try:
		with codecs.open(filename, 'r', encoding='utf-8', errors='ignore') as file_object:
			lines = file_object.readlines()

		for i, line in enumerate(lines):
			if re.search(r"build", line.lower()):
				for item in lines[max(i-0, 0):i+2]:
					revit_info = revit_info + item

		#get revit_build
		revit_build = revit_info.splitlines()[0]
		revit_build = revit_build.split(":",1)[1].strip()
		
		#get revit_build
		revit_branch = revit_info.splitlines()[1]
		revit_branch = revit_branch.split(":",1)[1].strip()
		
		#return values
		return revit_build, revit_branch
		
	except:
		print("***Could not gather REVIT info from", filename, "***")


def extract_info_username(filename):
	#pulls the username associated with the journal file into
	#variable username
	import re
	import codecs
	
	username = ""
	
	try:
		with codecs.open(filename, 'r', encoding='utf-8', errors='ignore') as file_object:
			lines = file_object.readlines()

		for i, line in enumerate(lines):
			if "jrn.directive" in line.lower() and "username" in line.lower(): 
				for item in lines[max(i-0, 0):i+2]:
					extracted_text = item.strip()
		values = re.findall('"([^"]*)"', extracted_text)
		username = values[0]
		return username
		
	except:
		print("***Could not gather USERNAME info from", filename, "***")


def extract_info_ram(filename):
	#parse a journal for ram information.
	
	#required modules
	import math
	import codecs
	
	#Variables to store journal info to.
	journal = ""
	ram_record = []
	
	try:
		#transform journal into parsable string
		with codecs.open(filename, 'r', encoding='utf-8', errors='ignore') as file_object:
			lines = file_object.readlines()
			for line in lines:
				journal = journal + line		
		journal = journal.splitlines()
		
		#Extract the lines that reference ram in the journal.
		for line in journal:
			if "ram statistics" in line.lower():
				data = line.split(':<')[1]
				ram_record.append([int(s) for s in data.split() if s.isdigit()][0])
				ram_max = [int(s) for s in data.split() if s.isdigit()][1]
		
		#Convert the extracted ram info into usable data.
		ram_max = math.floor(int(ram_max) / 1000)
		ram_avg = sum(ram_record) / len(ram_record) / 1000
		ram_avg = round(ram_avg, 2)
		ram_peak = sorted(ram_record)[-1] / 1000
		ram_peak = round(ram_peak, 2)
		
		return ram_max, ram_avg, ram_peak
	
	except:
		print("***Could not gather RAM info from", filename, "***")


def extract_info_commands(filename):
	#parses journal for jrn commands.

	#imports
	import math
	import codecs

	#create empty lists for data to be stored to.
	jrn_commands = []
	jrn_hotkeys = []
	commands_escape = []
	most_used_container = []

	#open journal as readable file
	with codecs.open(filename, 'r', encoding='utf-8', errors='ignore') as file_object:
		lines = file_object.readlines()
		
		#parse out lines containing 'jrn.command' from journal
		for i, line in enumerate(lines):
			if "jrn.command" in line.lower() and "above" not in line.lower() and "cancel the current operation" not in line.lower():
				jrn_commands.append(line.lower())
		
		#get how many times escape was pressed.
		for line in lines:
			if "cancel the current operation" in line.lower():
				commands_escape.append(line)
		 
	#get hotkey use percentage
	for line in jrn_commands:
		if "accelkey" in line.lower() or "shortcut" in line.lower():
			jrn_hotkeys.append(line.lower())

	#get dictionary of ordered commands.
	unique_commands = create_dict_command_occurence(filename)
	
	#get most used command
	for k, v in unique_commands.items():
		command = str(k)
		most_used_container.append(command)
		

	#store data to variables
	commands_total = len(jrn_commands)
	commands_hotkey = len(jrn_hotkeys)
	commands_hotkey_percentage = math.ceil((commands_hotkey / commands_total) * 100)
	commands_dynamo = str(jrn_commands).count("dynamo")
	commands_escape = len(commands_escape)
	most_used_command = most_used_container[0]

	#return variables
	return commands_total, commands_hotkey_percentage, commands_dynamo, unique_commands, commands_escape, most_used_command, jrn_commands


def print_commands_ordered(file_location):
	journals = cycle_journal_files(file_location)
	for item in journals:
		test = extract_info_commands(item)[3]
		print(filename)
		for k, v in test.items():
			print(v, k)
			
			
def create_dict_command_occurence(filename):
	'''creates a dictionary of all commands in a journal with 
		corresponding occurence value.'''
	
	#import required modules.	
	import codecs
	import re
	from operator import itemgetter
	
	#the file is opened and read.
	with codecs.open(filename, 'r', encoding='utf-8', errors='ignore') as file_object:
		lines = file_object.readlines()
		
		#container varialbles are created.
		non_repeating = []
		command_occurence_unordered = {}
		lowercase_lines = []
		command_occurence_ordered = {}
		
		#make all lines lowercase for better parsing.
		for line in lines:
			lowercase_lines.append(line.lower())	
		
		#filter out all lines with 'jrn.command'
		for line in lowercase_lines:
			if "jrn.command" in line.lower():
				if line.lower() not in non_repeating:
					non_repeating.append(line.lower())
				else:
					pass
			else:
				pass
				
		#cull all items that repeat, then add to list and count how many
		#times they repeated.
		for item in non_repeating:
			if "cancel the current operation" not in item:
				count = lowercase_lines.count(item)
				command_string = re.findall('"([^"]*)"', item)
				command_occurence_unordered[str(command_string)] = count
		
		#sort the dictionary so the most used commands are on top.
		for k, v in sorted(command_occurence_unordered.items(), key=itemgetter(1), reverse = True):
			if len(k.split()) > 1:
				command_occurence_ordered[k] = v
		
		#return the sorted dictionary.
		return command_occurence_ordered


def read_journal_data(file_location):
	#Reads off all of the gathered journals in a folder.
	
	for filename in cycle_journal_files(file_location):
		#journal name
		print("-----------------------------------------------------------")
		print(filename)
		#username
		try:
			print("User:", extract_info_username(filename))
		except:
			print("USER FAILED")
		#project_name
		try:
			print("Project Name:", extract_info_project_name_location(filename)[1])
		except:
			print("PROJECT NAME FAILED")
		#file_path
		try:
			print("File Path:", extract_info_project_name_location(filename)[0])
		except:
			print("FILE PATH FAILED")
		#date
		try:
			print("Date:", extract_info_date_time(filename)[0])
		except:
			print("DATE FAILED")
		#session_start
		try:
			print("Session start time:", extract_info_date_time(filename)[2])
		except:
			print("SESSION START TIME FAILED")
		#session_end
		try:
			print("Session end time:", extract_info_date_time(filename)[3])
		except:
			print("SESSION END TIME FAILED")
		#length of revit session
		try:
			print("Length of Revit session:", extract_info_date_time(filename)[4])
		except:
			print("LENGTH OF SESSION FAILED")
		#os info
		try:
			print("OS Version:", extract_info_os(filename)[0])
			print("OS Build:", extract_info_os(filename)[1])
		except:
			print("OS FAILED")
		#Revit info
		try:
			print("Revit Build:", extract_info_revit(filename)[0])
			print("Revit Branch:", extract_info_revit(filename)[1])
		except:
			print("REVIT FAILED")
		#cpu info
		try:
			print("CPU Name:", extract_info_cpu(filename)[0])
			print("CPU Clockspeed:", extract_info_cpu(filename)[1])
		except:
			print("CPU FAILED")
		#graphics info
		try:
			print("GPU Name:", extract_info_graphics(filename)["gpu_name"])
			print("GPU Manufacturer ID:", extract_info_graphics(filename)["gpu_manufacturer_id"])
			print("GPU Device ID:", extract_info_graphics(filename)["gpu_device_id"])
		except:
			print("GPU FAILED")
		#ram info
		try:
			print("RAM Max:", extract_info_ram(filename)[0], "GB")
			print("RAM Session Average:", extract_info_ram(filename)[1], "GB")
			print("RAM Peak Session:", extract_info_ram(filename)[2], "GB")
		except:
			print("RAM FAILED")
		#commands info
		try:
			print("Commands Total:", extract_info_commands(filename)[0])
			print("Commands Hotkey Percentage: " + str(extract_info_commands(filename)[1]) + "%")
			print("Commands Unique:", len(extract_info_commands(filename)[3]))
			print("Commands Dynamo:", extract_info_commands(filename)[2])
			print("Escape Key Pressed:", extract_info_commands(filename)[4])
			print("Most Used Command:", extract_info_commands(filename)[5])
				
		except:
			print("COMMANDS FAILED")
				
			
def compile_journal_list(file_location):
	#Compiles all journals in a folder into a list of dictionaries.

	count = 0
	journals = cycle_journal_files(file_location)

	for item in journals:
		try:
			filename = item
			username = extract_info_username(journals[count])
			try:
				project_name = extract_info_project_name_location(journals[count])[1]
			except:
				project_name = "depends on central"
			try:
				file_path = extract_info_project_name_location(journals[count])[0]
			except:
				file_path = "no central detected"
			try:
				journal_date = extract_info_date_time(journals[count])[0]
			except:
				journal_date = "error"
			try:
				start_time = extract_info_date_time(journals[count])[2]
			except:
				start_time = "error"
			try:
				end_time = extract_info_date_time(journals[count])[3]
			except:
				end_time = "journal write ended prematurely"
			try:
				session_length = extract_info_date_time(journals[count])[4]
			except:
				session_length = "error"
			try:
				os_version = extract_info_os(journals[count])[0]
			except:
				os_version = "error"
			try:
				os_build = extract_info_os(journals[count])[1]
			except:
				os_build = "error"
			try:
				revit_build = extract_info_revit(journals[count])[0]
			except:
				revit_build = "error"
			try:
				revit_branch = extract_info_revit(journals[count])[1]
			except:
				revit_branch = "error"
			try:
				cpu_name = extract_info_cpu(journals[count])[0]
			except:
				cpu_name = "error"
			try:
				cpu_clockspeed = extract_info_cpu(journals[count])[1]
			except:
				cpu_clockspeed = "error"
			try:
				gpu = extract_info_graphics(journals[count])
			except:
				gpu = ["error", "error", "error"]
			try:
				commands_total = extract_info_commands(journals[count])[0]
			except:
				commands_total = "error"
			try:
				commands_hotkey_percentage = extract_info_commands(journals[count])[1]
			except:
				commands_hotkey_percentage = "error"
			try:
				commands_unique = len(extract_info_commands(journals[count])[3])
			except:
				commands_unique = "error"
			try:
				commands_dynamo = extract_info_commands(journals[count])[2]
			except:
				commands_dynamo = "error"
			try:
				commands_escape_key = extract_info_commands(journals[count])[4]
			except:
				commands_escape_key = "error"
			try:
				commands_most_used = extract_info_commands(journals[count])[5]
			except:
				commands_most_used = "error"
			try:
				ram_max = extract_info_ram(journals[count])[0]
				ram_avg = extract_info_ram(journals[count])[1]
				ram_peak = extract_info_ram(journals[count])[2]
			except:
				ram_max = "error"
				ram_avg = "error"
				ram_peak = "error"
			
			journals[count] = {
				"filename" : filename,
				"username" : username,
				"project_name" : project_name,
				"file_path" : file_path,
				"date" : journal_date,
				"start_time" : start_time,
				"end_time" : end_time,
				"length_of_revit_session" : session_length,
				"os_version" : os_version,
				"os_build" : os_build,
				"revit_build" : revit_build,
				"revit_branch" : revit_branch,
				"cpu_name" : cpu_name,
				"cpu_clockspeed" : cpu_clockspeed,
				"gpu_name" : gpu["gpu_name"],
				"gpu_manufacturer_id" : gpu["gpu_manufacturer_id"],
				"gpu_device_id" : gpu["gpu_device_id"],
				"ram_max" : ram_max,
				"ram_avg" : ram_avg,
				"ram_peak" : ram_peak,
				"commands_total" : commands_total,
				"commands_hotkey_percentage" : commands_hotkey_percentage,
				"commands_unique" : commands_unique,
				"commands_dynamo" : commands_dynamo,
				"commands_escape_key" : commands_escape_key,
				"commands_most_used" : commands_most_used
						}
			count += 1
	
			
		except:
			count += 1
			pass
	
	return (journals)


def write_to_csv(file_location, journal_list, csv_name):
	#writes a list of journal dictionaries to a csv file.
	import csv

	myFile = open(csv_name, 'w')  
	with myFile:  
		myFields = ["filename", "username", "project_name", "file_path",
			"date", "start_time", "end_time", "length_of_revit_session",
			"os_version", "os_build", "revit_build", "revit_branch",
			"cpu_name", "cpu_clockspeed", "gpu_name", "gpu_manufacturer_id",
			"gpu_device_id", "ram_max", "ram_avg", "ram_peak",
			"commands_total", "commands_hotkey_percentage", "commands_unique",
			"commands_dynamo", "commands_escape_key", "commands_most_used"]
		writer = csv.DictWriter(myFile, fieldnames=myFields)    
		writer.writeheader()
		for item in journals:
			try:
				writer.writerow(item)
			except:
				print("error writing data to:", item)



#Execute


filename = 'journal.0012.txt'
'''
filename = 'journal.0012.txt'
test = extract_info_commands(filename)[3]
#test = create_dict_command_occurence(filename)
for item in test:
	print(item)
sumval = sum(test.values())
print(sumval)
'''

'''
test = compile_journal_list('.')

print(test)

'''

#read_journal_data('.')


journals = compile_journal_list('.')
write_to_csv('.', journals, 'christian.csv')



'''
test = extract_info_commands(filename)[5]
print(test)
'''	
