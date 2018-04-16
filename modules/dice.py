from random import randint

class Dice():
	#Initialize a single die.
	def __init__(self, sides=6):
		self.sides = sides
		
	def roll(self, number_of_rolls=1):
		#Rolls the die specified number of times
		self.number_of_rolls = number_of_rolls
		roll_count = 0
		roll_memory = []
		while roll_count < self.number_of_rolls:
			roll_count += 1
			current_roll = randint(1, self.sides)
			print("D" + str(self.sides) + ":" + " Rolls for " + str(current_roll))
			roll_memory.append(current_roll)
		#If the die is rolled more than once, the rolls will be calculated.
		if number_of_rolls > 1:
			print("For a total of", str(sum(roll_memory)))

d6 = Dice(6)

d6.roll(2)

d20 = Dice(20)

d20.roll(100)

