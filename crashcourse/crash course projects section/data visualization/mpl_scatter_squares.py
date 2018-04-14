import matplotlib.pyplot as plt

def find_square_value(initial_values):
	#find the square value of a list of numbers.
	square_values = []
	for i in initial_values:
		i = i **2
		square_values.append(i)
	return(square_values)
	
	
plt.scatter(2, 4)
plt.show()
