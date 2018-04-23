
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
	return journal_files


def extract_info_processor(filename):
	#parses journal for processor information.
	import re
	
	processor_info = ""
	
	try:
		with open(filename, 'r') as file_object:
			lines = file_object.readlines()

		for i, line in enumerate(lines):
			if re.search(r"processor information:", line.lower()):
				for item in lines[max(i-0, 0):i+19]:
					if "name" in item.lower() or "maxclockspeed" in item.lower() and item not in processor_info:
						processor_info = processor_info + item
					else:
						continue
						
		processor_info = processor_info.splitlines()
		
		for item in processor_info:
			if "name" in item.lower():
				processor_name = item
				processor_name = processor_name.split(":",2)[2].strip()

		for item in processor_info:
			if "maxclockspeed" in item.lower():
				processor_clockspeed = item
				processor_clockspeed = processor_clockspeed.split(":",2)[2].strip()
				processor_clockspeed = int(processor_clockspeed) / 1000
				
		return processor_name, processor_clockspeed
		
	except:
		print("***Could not gather PROCESSOR info from", filename, "***")


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
					graphics_hardware["graphics card:"] = values[0]
					graphics_hardware["manufacturer id:"] = values[1]
					graphics_hardware["device id:"] = values[2]
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
		ram_peak = sorted(ram_record)[-1] / 1000
		
		return ram_max, ram_avg, ram_peak
	
	except:
		print("***Could not gather RAM info from", filename, "***")
	
#execute
for filename in cycle_journal_files('.'):
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
	#processor info
	try:
		print("Processor Name:", extract_info_processor(filename)[0])
		print("Processor Clockspeed:", extract_info_processor(filename)[1])
	except:
		print("PROCESSOR FAILED")
	#graphics info
	try:
		print("GPU Name:", extract_info_graphics(filename)["graphics card:"])
		print("GPU Manufacturer ID:", extract_info_graphics(filename)["manufacturer id:"])
		print("GPU Device ID:", extract_info_graphics(filename)["device id:"])
	except:
		print("GPU FAILED")
	#ram info
	try:
		print("Max System RAM:", extract_info_ram(filename)[0], "GB")
		print("Session Average RAM:", extract_info_ram(filename)[1], "GB")
		print("Peak Session RAM:", extract_info_ram(filename)[2], "GB")
	except:
		print("RAM FAILED")






