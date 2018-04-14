"""animals = ["Sheep", "Tiger", "Bear"]

for animal in animals:
	print(animal, "you shit the goddam bed again!")
	print("I will fucking end you!")
	
print("Son of a christ, I hate these animals.")



pizzas = ["supreme", "veggie", "meat lovers"]
for pizza in pizzas:
	print("I am not a huge fan of", pizza, "pizza.")
print("In fact, I hate these toppings so goddam much,\nthat I won't even feed them to the homeless!\nI said it...")
	
numbers = list(range(0, 500))

print(numbers)

plusOne = []

for number in numbers:
	plusOne.append(number+1)
	
print(plusOne)

numberscompression = [number +1 for number in range(0, 100)]

print(numberscompression) """

"""numbers = []
for number in range(1,1001,7):
	number = number**3
	numbers.append(number)
	
print(numbers)

numberscompression = [number**3 for number in range(1,1000001)]
print(numberscompression
numbers2 = numbers[:]

numbers.append(74)
numbers2.append(75)

print(numbers)
print(numbers2) 

myList = ["granola", "whales", "charizard", "allen wrench", "hovercraft", "snow globe", "yellow", "juice box", "polio"]

print(str(myList).title())

print("The first three items on my list are", myList[:3])
print("Three items in the middle of my list are", myList[3:6])
print("The last three items on my list are", myList[-3:])

yourList = myList[:]

myList.append("Pnus")

yourList.append("Vagenus")

print(myList)
print(yourList)

for myItems in myList:
	print(myItems)
	
for yourItems in yourList:
	print(yourItems)
	
myTuple = ("taco", "enchilada", "burrito", "nacho", "soapapilla")

print(myTuple)

myTuple = ("quesadilla", "enchilada", "chorizo", "nacho", "queso")
food = ""
for food in myTuple:
	print(food)
	
topping = input("What topping would you like?")
topping = topping.lower()
if topping != "anchovies":
	print("NO ANCHOVIES!")
else:
	print("Ewwww, anchovies.") """
	
age = 16
age2 = 17

idolAquired = True

if age > 18 or age2 > 21:
	print("Okay to play")
else:
	print("Get out of here kid!")

if idolAquired == False:
	print("Proceed to level 2")
else:
	print("Find the Idol before proceeding!")

print("Has the idol been aquired yet? I predict True.")
print(idolAquired == True)

print("Is age equal to 19? I predict False")
print(age == 18)

print("Has idol been aquired or age is equal to 18? I predict True")
print(idolAquired == True or age == 18)

name = "Johnathan"
name = name.lower()

print(name)
print(name == "johnathan")
	
