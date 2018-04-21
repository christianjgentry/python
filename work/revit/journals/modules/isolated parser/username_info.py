import os
import re


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

def extract_info_hardware_graphics(filename):
	graphics_hardware = {}
	with open(filename, 'r') as file_object:
		file_object = file_object.read()
		file_object = file_object.lower().splitlines()
		for line in file_object:
			if "username" in line:
				values = re.findall('"([^"]*)"', line)
				graphics_hardware["graphics card:"] = values[0]
				#graphics_hardware["manufacturer id:"] = values[1]
				#graphics_hardware["device id:"] = values[2]
		return graphics_hardware

#print(cycle_journal_files('.'))

'''

for value in cycle_journal_files('.'):
	filename = value
	print(extract_info_hardware_graphics(filename))

'''

with open('journal.0013.txt', 'r') as file_object:
    lines = file_object.readlines()

for i, line in enumerate(lines):
	if "jrn.directive" in line.lower() and "username" in line.lower(): 
		for item in lines[max(i-0, 0):i+2]:
			print(item.strip())
			
            
            
            
            
            
            
            
            
            
