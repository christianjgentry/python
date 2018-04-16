import matplotlib.pyplot as plt

def find_square_value(initial_values):
	#find the square value of a list of numbers.
	square_values = []
	for i in initial_values:
		i = i **2
		square_values.append(i)
	return(square_values)
	
#data to plot.
x_values = list(range(1, 1001))
y_values = find_square_value(x_values)

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
	edgecolor='none', s=20)

#set chart title and  label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#set the range for each axis.
plt.axis([0, 1100, 0, 1100000])

#Set plot tick labels
plt.tick_params(axis="both", which="major", labelsize=14)

#Show the plot
plt.show()
