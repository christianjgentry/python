'''
a module that allows for users to parse Revit Journal files for
useful data.

module commonly imported as jparse
'''

#imports
import json
import pathlib
import os
import re
import csv
##########################################################################################
#classes
class User():
	#Class that models a Revit user
	
	def __init__(self, username):
		'''initializes the class with a username, additional info
		   gathered after initialization'''
		self.username = username
		self.title = ""
		self.journal_log = {}
	
	def get_dict(self):
		#gets the dictionary associated with class instance.
		self.dict = {	
		"username" : self.username,
		"title" : self.title,
		"journal_log" : self.journal_log,
					}
		return self.dict
	
	def append_journal_files(self, directory_in_str):
		#appends all items of filetype in folder to dictionary instance.
		directory = os.fsencode(directory_in_str)
		enumerated_journal = ""
		for file in os.listdir(directory):
			filename = os.fsdecode(file)
			if filename.endswith(".txt") and "dump" not in filename:
				pathname = os.path.join(directory_in_str, filename)
				with open(pathname, 'r') as file_object:
					if filename not in self.journal_log.keys():
						for line in enumerate(file_object.readlines()):
							enumerated_journal += str(line) + "\n"
						self.journal_log[filename] = enumerated_journal
					else:
						continue
				continue
			else:
				continue


	
	
#functions
def read_journal_enumerated(filename_journal):
	#reads an enumerated journal file.
	enumerated_journal = ""
	with open(filename_journal, 'r') as file_object:
		for line in enumerate(file_object.readlines()):
			enumerated_journal += str(line) + "\n"
	return enumerated_journal			

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

def extract_info_hardware_graphics(filename):
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

##########################################################################################
#execute

#print(cycle_journal_files('./Journals'))
'''
journal_files = cycle_journal_files('./Journals')
with open('csv_export_test.csv', 'w') as new_csv:
	fieldnames = ['journal_entry']
	csv_writer = csv.DictWriter(new_csv, fieldnames=fieldnames)
	csv_writer.writeheader()
	csv_writer.writerow(journal_files)
'''	

christian = User("christian")
location ='.\Journals'			       

christian.append_journal_files(location)
print(christian.journal_log.keys())


'''
for key in christian.journal_log.keys():
	print(extract_info_hardware_graphics(christian.journal_log[key]))
'''

#print(extract_info_hardware_graphics('journal.0028.txt'))
