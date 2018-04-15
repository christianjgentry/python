import matplotlib.pyplot as plt
from mpl_random_walk import RandomWalk


while True:
	#make random walk and plot the points.
	rw = RandomWalk()
	rw.fill_walk()
	plt.plot(rw.x_values, rw.y_values, linewidth=1)
	plt.show()

	keep_running = input("Make a new walk? (y/n): ")
	if keep_running == 'n':
		break
