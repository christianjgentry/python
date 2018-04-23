def cycle_journal_files(directory_in_str):
	#appends all journal files in folder to list journal_files.
	import os
	
	journal_files = []
	directory = os.fsencode(directory_in_str)
	for file in os.listdir(directory):
		filename = os.fsdecode(file)
		if filename.endswith(".txt") and "dump" not in filename:
			journal_files.append(filename)
			continue
		else:
			continue
	return journal_files



def extract_info_ram(filename):
	#parse a journal for ram information.
	
	#required modules
	import math
	
	#Variables to store journal info to.
	journal = ""
	ram_record = []
	
	#transform journal into parsable string
	with open(filename, 'r') as file_object:
		lines = file_object.readlines()
		for line in lines:
			journal = journal + line		
	journal = journal.splitlines()
	
	#Extract the lines that reference ram in the journal.
	for line in journal:
		if "ram statistics" in line.lower():
			data = line.split(':<')[1]
			ram_record.append([int(s) for s in data.split() if s.isdigit()][0])
			ram_max = [int(s) for s in data.split() if s.isdigit()][1]
	
	#Convert the extracted ram info into usable data.
	ram_max = math.floor(int(ram_max) / 1000)
	ram_avg = math.ceil(sum(ram_record) / len(ram_record))
	ram_peak = sorted(ram_record)[-1]
	
	return ram_max, ram_avg, ram_peak

journal_files = cycle_journal_files('.')

for filename in journal_files:
	print(filename)
	print(extract_info_ram(filename))


'''

import matplotlib.pyplot as plt


max_ram = 32751

def ram_percentage(dataset):
	percentage_list = []
	for value in dataset:
		percentage = value / max_ram
		percentage *= 100
		percentage = math.ceil(percentage)
		percentage_list.append(percentage)
	return(percentage_list)

ram_record = []
with open(filename, 'r') as f:
	for line in f:
		line = line.lower()
		if 'ram statistics' in line:
			data = line.split(':<')[1]
			ram_record.append([int(s) for s in data.split() if s.isdigit()][0])
ram_percentages = ram_percentage(ram_record)
print(ram_percentages)
print(ram_record)


plt.plot(range(1, 26, 1), ram_percentages, c='red', linewidth = 5)

plt.title("RAM Usage Throughout Revit Session", fontsize=24)
plt.xlabel("Datapoint", fontsize=14)
plt.ylabel("RAM Percentage Used", fontsize=14)

#Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)
plt.xticks(range(1,26))

plt.show()
'''
