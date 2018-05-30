'''
while True:
		
	age = "How old are you?"
	age += "\nI need to know if you are old enough to vote."

	age = input(age)

	print(age)
'''
'''
########################################################################
var = 0

while var <= 100:
	var +=1
	
	if var % 4 == 0:
		print("skip")
	
	elif var % 9 == 0:
		print("CRITICAL")
	
	else:
		print(var)
########################################################################		
'''

'''
########################################################################	
car = input("What kind of car would you like?: ")

print(car + "\nI'll try to find you a", car + ".")

########################################################################	
'''
'''
########################################################################	
party = input("How many people are in your dinner party?: ")
party = int(party)

if party < 8:
	print("Your table is ready")
	
elif party >= 8:
	print("You will have to wait for a table.")
########################################################################	
'''
########################################################################	
'''
variable = input("enter a number. I will determine if it is a multiple of 10 or not.")
variable = int(variable)

if variable % 10 == 0:
	print(variable, "is a multiple of 10!")
else:
	print(variable, "is not a multiple of 10 :(")
'''
########################################################################	
'''
hp = 100
cities = 3
message = ""
gameOn = True

while gameOn == True:
	hp = input("enter hp: ")
	hp = int(hp)
	print(hp)
	cities = input("enter cities: ")
	cities = int(cities)
	print(cities)
	message = input("enter message: ")
	print(message)
	
	if hp == 0:
		gameOn = False
	if cities == 0:
		gameOn = False
	if message == "quit":
		gameOn = False

print("Game Over")
'''
########################################################################	
'''
count = 0

while count <= 10:
	count += 1
	if count % 2 == 0:
		print(count)
'''
########################################################################	

sandwich_orders = ["blt", "pastrami", "pb&j", "grilled cheese", "pastrami", "ham & cheese",
	"turkey", "tuna", "pastrami"]
finished_sandwich = []

print("Sorry! The deli has run out of pastrami.\n")

while "pastrami" in sandwich_orders:
	sandwich_orders.remove("pastrami")

while len(sandwich_orders) > 0:
	current_sandwich = sandwich_orders.pop()
	print("I have finished making the", current_sandwich, "sandwich!")
	finished_sandwich.append(current_sandwich)
	
print("\nI have finished making all of the sandwiches!")


