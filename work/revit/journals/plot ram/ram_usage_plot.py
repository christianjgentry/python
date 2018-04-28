from datetime import datetime
from operator import itemgetter
import matplotlib.pyplot as plt
import math

#Revit Journal Read Test
filename = 'journal.0013.txt'

'''
journal = []
with open(filename, 'r') as f:
	for line in enumerate(f.readlines()):
		print(line)

'''
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

'''
'''
with open(filename, 'r') as f:
	journal = f.readlines()
	
	for line in journal:
		if "warning" in line.lower():
			print(line)
		
'''
'''
with open(filename, 'r') as file_object:
			lines = file_object.read().lower()
			split_lines = lines.split()
			non_repeating = []
			word_occurence = {}	
			
			for word in split_lines:
				if word not in non_repeating:
					non_repeating.append(word)
				else:
					pass
			
			for item in non_repeating:
				count = split_lines.count(item)
				word_occurence[item] = count


dictionary = sorted(word_occurence.items(), key=itemgetter(1))


print(dictionary)
'''

'''
with open(filename, 'r') as f:
	for line in f.readlines():
		if 'jrn.command' in line.lower():
			print(line)
'''

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

