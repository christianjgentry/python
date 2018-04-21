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


'''
with open('journal.0013.txt', 'r') as file_object:
    lines = file_object.readlines()

for i, line in enumerate(lines):
    if re.search(r"operating system info", line.lower()):
        for item in lines[max(i-0, 0):i+20]:
			
            print(item.rstrip())
'''	

def extract_os_info(filename):
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

#execute

os_info = extract_os_info('journal.0013.txt')

print("OS Version:", os_info[0])
print("OS Build Number:", os_info[1])
