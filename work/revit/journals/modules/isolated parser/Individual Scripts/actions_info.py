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








action_count = 0
with open('journal.0013.txt', 'r') as file_object:
	file_object = file_object.readlines()
	for line in file_object:
		if "jrn." in line.lower():
			print(line)
			action_count += 1
print(action_count)


            
            
            
            
            
