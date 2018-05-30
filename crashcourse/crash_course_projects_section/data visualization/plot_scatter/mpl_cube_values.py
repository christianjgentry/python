import matplotlib.pyplot as plt

def cubed_values(initial_values):
	#returns cubed values of numbers in initial_values list
	cubed_values = []
	for i in initial_values:
		i = i ** 3
		cubed_values.append(i)
	return cubed_values

x_values = list(range(1, 5000))
y_values = cubed_values(x_values)

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=5)

plt.show()
