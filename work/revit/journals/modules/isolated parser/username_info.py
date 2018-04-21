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


def extract_username(filename):
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


for item in cycle_journal_files('.'):
	print(extract_username(item))


            
            
            
            
            
