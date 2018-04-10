animals = []

maxListLength = 5

while len(animals) < maxListLength:
	addAnimal = input("Let's add an animal to the list! Name an animal: ")
	animals.append(addAnimal) 
else:
	len(animals) > maxListLength
	print("All Done!")
	print(animals)
