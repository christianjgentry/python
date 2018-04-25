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


def extract_info_cpu(filename):
	#parses journal for cpu information.
	import re
	
	cpu_info = ""
	
	try:
		with open(filename, 'r') as file_object:
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
	
	os_info = ""
	
	try:
		with open(filename, 'r') as file_object:
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
	
	graphics_hardware = {}
	
	try:
		with open(filename, 'r') as file_object:
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
	
	revit_info = ""
	
	try:
		with open(filename, 'r') as file_object:
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
	
	username = ""
	
	try:
		with open(filename, 'r') as file_object:
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
	
	#Variables to store journal info to.
	journal = ""
	ram_record = []
	
	try:
		#transform journal into parsable string
		with open(filename, 'r') as file_object:
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
			print("cpu FAILED")
		#graphics info
		try:
			print("GPU Name:", extract_info_graphics(filename)["graphics card:"])
			print("GPU Manufacturer ID:", extract_info_graphics(filename)["manufacturer id:"])
			print("GPU Device ID:", extract_info_graphics(filename)["device id:"])
		except:
			print("GPU FAILED")
		#ram info
		try:
			print("RAM Max:", extract_info_ram(filename)[0], "GB")
			print("RAM Session Average:", extract_info_ram(filename)[1], "GB")
			print("RAM Peak Session:", extract_info_ram(filename)[2], "GB")
		except:
			print("RAM FAILED")
				

def compile_journals_dict(file_location):
	#Compiles all journals in a folder into a list of dictionaries.

	count = 0
	journals = cycle_journal_files(file_location)

	for item in journals:
		filename = item
		username = extract_info_username(journals[count])
		os_version = extract_info_os(journals[count])[0]
		os_build = extract_info_os(journals[count])[1]
		revit_build = extract_info_revit(journals[count])[0]
		revit_branch = extract_info_revit(journals[count])[1]
		cpu_name = extract_info_cpu(journals[count])[0]
		cpu_clockspeed = extract_info_cpu(journals[count])[1]
		gpu = extract_info_graphics(journals[count])
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
						}
		count += 1
	
	return (journals)



#Execute

file_location = '.'
journals = compile_journals_dict(file_location)

print(journals)


