from data_visualization_dice_module import *
import pygal

#create a d6
d6_1 = Dice(6)
d6_2 = Dice(6)
d6_3 = Dice(6)

#Make some rolls and then store those rolls in a list.
results = []

for roll in range(5000):
	roll = d6_1.roll() + d6_2.roll() + d6_3.roll()
	results.append(roll)
	
#Analyze the results
frequencies = []
max_result = d6_1.sides * 3
for value in range(3, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)	
	
print(frequencies)

#Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling three D6 1000 times"
hist.x_labels = []
for i in range(3, max_result+1):
	hist.x_labels.append(i)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6+D6+D6', frequencies)
hist.render_to_file('die_visual.svg')
