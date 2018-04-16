from wordcount_module import *
from operator import itemgetter
import matplotlib.pyplot as plt


word_count('brothers_grimm_fairytales.txt')


dictionary = word_occurence_dict('brothers_grimm_fairytales.txt')

dictionary = sorted(dictionary.items(), key=itemgetter(1))

dictionary = dictionary[-10:-1]

value_list = []


for item in dictionary:
	value_list.append(item[1])

get_sum = sum(value_list)

labels = []
for key in dictionary:
	labels.append(str(key))
	
total_occurences = []
for value in dictionary:
	total_occurences.append(value)


sizes = []

def calculate_percentage(percentage_list):
	for value in value_list:
		percentage = value / get_sum
		percentage_list.append(percentage)
		
calculate_percentage(sizes)		
	
	

	

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
