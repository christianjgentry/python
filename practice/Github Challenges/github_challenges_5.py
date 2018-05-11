'''
Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''

class Sentence():
	def __init__(self):
		self.words = ""
		
	def get_string(self):
		self.words = input("Enter a word or sentence: ")
		
	def print_string(self):
		print(self.words)
		
		
test = Sentence()

test.get_string()

test.print_string()
