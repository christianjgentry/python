filename_cats = 'cats.txt'
filename_dogs = 'dogs.txt'


try:
	with open(filename_cats, 'r') as file_object:
		cats_lines = file_object.readlines()
		for line in cats_lines:
			print(line.rstrip())

	print("\n")

	with open(filename_dogs, 'r') as file_object:
		dogs_lines = file_object.readlines()
		for line in dogs_lines:
			print(line.rstrip())
			
except FileNotFoundError:
	print("Oops! One of your file paths appears to be incorrect.",
		"Go back and make sure that your files are pathed correctly!")

	
	
