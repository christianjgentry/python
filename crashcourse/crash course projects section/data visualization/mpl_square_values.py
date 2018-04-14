import matplotlib.pyplot as plt

def find_square_value(initial_values):
	#find the square value of a list of numbers.
	square_values = []
	for i in initial_values:
		i = i **2
		square_values.append(i)
	return(square_values)
	
	
input_values = [1, 2, 3, 4, 6, 7, 8, 9, 10]
squares = find_square_value(input_values)
plt.plot(input_values, squares, linewidth = 5)



#Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)

plt.show()

