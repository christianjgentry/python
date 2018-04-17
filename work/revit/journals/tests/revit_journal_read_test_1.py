import dateutil.parser as dparser

#Revit Journal Read Test
filename = 'journal.0033.txt'
'''
journal = []
with open(filename, 'r') as f:
	for line in enumerate(f.readlines()):
		print(line)

'''

with open(filename, 'r') as f:
	journal = f.readlines()
	
	for line in journal:
		if "Apr" and "Exit" in line:
			print(line)
