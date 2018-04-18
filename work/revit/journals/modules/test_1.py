import pathlib
import journal_parser as jparse
import re

filename = jparse.read_journal_enumerated('journal.0013.txt')

def extract_info_hardware_graphics(filename):
	graphics_hardware = {}
	filename = filename.lower().splitlines()
	for line in filename:
		if "video card environment" in line:
			values = re.findall('"([^"]*)"', line)
			graphics_hardware["graphics card:"] = values[0]
			graphics_hardware["manufacturer id:"] = values[1]
			graphics_hardware["device id:"] = values[2]
	return graphics_hardware

print(extract_info_hardware_graphics(filename))

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

'''
