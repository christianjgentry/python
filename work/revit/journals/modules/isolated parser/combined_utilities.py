import os
import re

#definitions
def cycle_journal_files(directory_in_str):
	#appends all journal files in folder to list journal_files.
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
	processor_info = ""
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


def extract_info_os(filename):
	#parses journal for os information.
	os_info = ""
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


def extract_info_graphics(filename):
	#parses journal for graphics hardware info.
	graphics_hardware = {}
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


def extract_info_revit(filename):
	#parses journal for Revit info.
	revit_info = ""
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


def extract_info_username(filename):
	#pulls the username associated with the journal file into
	#variable username
	username = ""
	with open(filename, 'r') as file_object:
		lines = file_object.readlines()

	for i, line in enumerate(lines):
		if "jrn.directive" in line.lower() and "username" in line.lower(): 
			for item in lines[max(i-0, 0):i+2]:
				extracted_text = item.strip()
	values = re.findall('"([^"]*)"', extracted_text)
	username = values[0]
	return username
	
	
#execute
for filename in cycle_journal_files('.'):
	#journal name
	print("-----------------------------------------------------------")
	print(filename)
	#username
	print("User:", extract_info_username(filename))
	#os info
	print("OS Version:", extract_info_os(filename)[0])
	print("OS Build:", extract_info_os(filename)[1])
	#Revit info
	print("Revit Build:", extract_info_revit(filename)[0])
	print("Revit Branch:", extract_info_revit(filename)[1])
	#processor info
	print("Processor Name:", extract_info_processor(filename)[0])
	print("Processor Clockspeed:", extract_info_processor(filename)[1])
	#graphics info
	print("GPU Name:", extract_info_graphics(filename)["graphics card:"])
	print("GPU Manufacturer ID:", extract_info_graphics(filename)["manufacturer id:"])
	print("GPU Device ID:", extract_info_graphics(filename)["device id:"])







