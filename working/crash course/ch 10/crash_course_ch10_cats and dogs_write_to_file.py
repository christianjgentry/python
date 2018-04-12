filename_cats = 'cats.txt'
filename_dogs = 'dogs.txt'

cat_names = ["jasmine", "whiskers", "ragamuffin"]
dog_names = ["scooter", "sparky", "mocha", "chipotle", "jesse bell",
"tinker"]

for cat in cat_names:
	with open(filename_cats, 'a') as file_object:
		file_object.write(str(cat + "\n"))
		
for dog in dog_names:
	with open(filename_dogs, 'a') as file_object:
		file_object.write(str(dog + "\n"))
