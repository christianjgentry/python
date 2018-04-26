import os
import re

'''
#Appends filenames to dictionar under single key.
def cycle_journal_files(directory_in_str):
	#prints a list of all journal files in a folder.
	journal_files = {}
	directory = os.fsencode(directory_in_str)
	for file in os.listdir(directory):
		filename = os.fsdecode(file)
		if filename.endswith(".txt"):
			journal_files.setdefault('journal_entry', []).append(filename)
			continue
		else:
			continue
	return journal_files
	'''

def cycle_journal_files(directory_in_str):
	#appends all journal files in folder to a list.
	journal_files = []
	directory = os.fsencode(directory_in_str)
	for file in os.listdir(directory):
		filename = os.fsdecode(file)
		if filename.endswith(".txt"):
			journal_files.append(filename)
			continue
		else:
			continue
	return journal_files

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



for value in cycle_journal_files('.'):
	filename = value
	print(extract_info_graphics(filename))

