'''
a module that allows for users to parse Revit Journal files for
useful data.

module commonly imported as jparse
'''

#imports
import json
import os


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
		for file in os.listdir(directory):
			filename = os.fsdecode(file)
			if filename.endswith(".txt"):
				pathname = os.path.join(directory_in_str, filename)
				with open(pathname, 'r') as file_object:
					if filename not in self.journal_log.keys():
						self.journal_log[filename] = file_object.readlines()
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
	directory = os.fsencode(directory_in_str)

	for file in os.listdir(directory):
		filename = os.fsdecode(file)
		if filename.endswith(".txt"): 
			print(filename)
			continue
		else:
			continue


christian = User("christian")

location = 'C:\\Users\Christian Gentry\AppData\Local\Autodesk\Revit\Autodesk Revit 2018\Journals'			       

christian.append_journal_files(location)

print(christian.journal_log.keys())

#cycle_journal_files(location)


