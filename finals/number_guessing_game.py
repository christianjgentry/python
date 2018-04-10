#These are the elements I am importing.
import math
import random
import sys

# I am storing my game variables here so that they load before the user assigns in input.
randomNumber = random.randrange(0, 100, 1)
totalInput = 0


#This is the initial user input. This is where the player decides if they would like to play the game or not.
while True:
	start = input("Would you like to play a game? yes or no:")
	if start == "yes":
		print("Awesome!")
		break	
	elif start == "no":
		print("Aww okay. I hope we play later!")
		sys.exit()
	else:
		print("Please enter a valid input!")


#If the player decides to play the game, this is where they will guess numbers until they guess the right one.
name = input("What is your name?: ")
print("Hello", name + "!")
if name == "Chantel":
	print("What a pretty name.")
print("I am thinking of a number betwen 0 and 100. Can you guess my number?")

while True:
	totalInput += 1
	userInput = input("Enter a number between 0-100: ")
	if int(userInput) == randomNumber:
		print("Good Job! You guessed my number!")
		print("It took you", str(totalInput), "tries to guess my number!")
		sys.exit()
	elif int(userInput) <= randomNumber:
		print("Too small. Try again.")
	else:
		int(userInput) >= randomNumber
		print("Too large. Try again.")
		
