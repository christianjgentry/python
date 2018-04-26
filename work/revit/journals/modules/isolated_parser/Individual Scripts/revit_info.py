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



def extract_revit_info(filename):
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

#execute

filename = 'journal.0013.txt'


print("Revit Build:", extract_revit_info(filename)[0])
print("Revit Branch", extract_revit_info(filename)[1])






