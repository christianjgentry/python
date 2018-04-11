filename = 'pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()
	


pi_string = ""
for line in lines:
	pi_string += line.strip()
	
birthday = input("enter your birthday in this format: mmddyy\n")

if birthday in pi_string:
	print("Your birthday is in the first million digits of pi!")
else:
	print("Sorry, your birthday is not in the first million digits of pi.")
