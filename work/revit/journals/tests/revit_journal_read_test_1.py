from datetime import datetime
from dateutil.parser import parse

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
		if "2018" and "started recording" in line:
			d1 = line
		if "2018" and "finished recording" in line:
			d2 = line


FMT = '%H:%M:%S'

tdelta = datetime.strptime(d1, FMT)

print(tdelta)
