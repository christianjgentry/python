import os
import re


def cycle_journal_files(directory_in_str):
	#appends all journal files in folder to list journal_files.
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



def extract_processor_info(filename):
	processor_info = ""
	with open(filename, 'r') as file_object:
		lines = file_object.readlines()

	for i, line in enumerate(lines):
		if re.search(r"processor information:", line.lower()):
			for item in lines[max(i-0, 0):i+19]:
				if item not in processor_info:
					processor_info = processor_info + item
				else:
					continue
	
	
	
	#get processor_name
	processor_name = processor_info.splitlines()[12]
	processor_name = processor_name.split(":",2)[2].strip()
	
	#get processor_clockspeed
	processor_clockspeed = processor_info.splitlines()[11]
	processor_clockspeed = processor_clockspeed.split(":",2)[2].strip()
	processor_clockspeed = str(int(processor_clockspeed) / 1000) + " GHz"
	
	#return values
	return processor_name, processor_clockspeed

#execute

filename = 'journal.0013.txt'


print(extract_processor_info(filename))







