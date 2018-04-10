########################################################################
'''
def greet_user(username):
	print("greetings", username)
	
name = "Christian"
greet_user(name)

def favorite_book(username, title):
	print(username + "'s favorite book is", title)

favorite_book(name, "It")
'''
########################################################################
'''
users = []

def add_user():
	user_count = input("how many users will you be adding?: ")
	user_count = int(user_count)
	user_add = 0
	username = ""
	while user_add < user_count:
		user_add += 1
		username = input("Enter a username: ")
		users.append(username)

add_user()

print("Thank you. These users have been added to the system.\n" + str(users))
'''
########################################################################
'''
def add_character(name = "unnamed", hp = 50, atk = 8):
	print(name + ":", "hp=", str(hp), "atk= ", str(atk))
	
add_character(atk = 100)
'''
########################################################################
'''
def make_shirt(size = "large", text = "I love Python" ):
	print(size, text)

make_shirt(text = "small")
'''	
########################################################################
'''
def full_name(first, last):
	first = first.lower()
	last = last.lower()
	full_name = first + " "+ last
	return full_name.title()

friend = full_name("christian", "GENTRY")

print(friend)
'''
########################################################################
'''
def find_area(length, width):
	area = length * width
	return area
	
	
room = find_area(10, 5)

print(room)
'''
########################################################################
'''
def city_country(city, country):
	formatted = str(city.title()) + ", " + str(country.title())
	return formatted
	
print(city_country("madrid", "spain"))
print(city_country("chicago", "united states"))
print(city_country("paris", "france"))
'''
########################################################################
'''
def make_album(artist, album, tracks=0):
	album_dict = {
	"artist" : artist,
	"album" : album,
		}
	if tracks:
		album_dict["tracks"] = tracks
	return album_dict

print(make_album("my chemical romance", "the black parade", 9))
print(make_album("fall out boy", "folie a deux", 12))
print(make_album("brand new", "the devil and god are raging inside me"))
'''
########################################################################
'''
artist_prompt = "What artist are you thinking of?: "
album_prompt = "What album are you thinking of?: "

print("Type 'quit' to quit at any time.")


while True:
	
	artist = input(artist_prompt)
	if artist == 'quit':
		break 
		
	album = input(album_prompt)
	if album == 'quit':
		break
	
	compile_album = make_album(artist, album)
	print(compile_album)
'''
########################################################################
''''
#initial model lists
models = ["car", "ring", "phone case", "bolt"]
completed_models = []

#definitions written here
def print_models(incomplete_model_list, complete_model_list):
	while models:
		current_model = incomplete_model_list.pop()
		print("Now printing,", current_model + "...")
		complete_model_list.append(current_model)
		print(current_model, "completed!\n")

def show_completed_models(complete_model_list):
	print("These models have been completed!\n", complete_model_list)
	
#definitions called here
print_models(models, completed_models)
show_completed_models(completed_models)
'''
########################################################################
'''
import math
import random

magicians = ["Lance", "Henry", "Chris", "David", "Nolan"]

def show_magicians(magician_list):
	while magician_list:
		random_title = random.randint(1,4)
		if random_title == 1:
			random_title = "the Great"
		elif random_title == 2:
			random_title = "the Magnificent"
		elif random_title == 3:
			random_title = "the Mysterious"
		elif random_title == 4:
			random_title = "the Wonderful"
		random_title = str(random_title)
		current_magician = magician_list.pop()
		print("Introducing", current_magician, random_title + "!")
	print("Give these fabulous performers a round of applause!")

show_magicians(magicians)
'''
########################################################################
'''
magicians = ["Lance", "Henry", "Chris", "David", "Nolan"]

def show_magicians(magician_list):
	while magician_list:
		current_magician = magician_list.pop()
		print("Introducing", current_magician + "!")
	print("Give these fabulous performers a round of applause!")
	
def make_great(magician_list):
	for magician in magician_list:
		magician = magician_list.pop()
		magician = "The Great " + str(magician)
		magician_list.insert(0, magician)

show_magicians(magicians[:])	
make_great(magicians)
show_magicians(magicians)
'''
########################################################################
'''
def make_pizza(size, *toppings):
	print("Making a", str(size) + "-inch pizza with:")
	for topping in toppings:
		print("-", topping)
	print("\n")

make_pizza(12, "peperonni")
make_pizza(16, "cheese", "pineapple", "sausage")
'''
########################################################################
'''
def add_sandwich_toppings(*toppings):
	sandwich_toppings = []
	for topping in toppings:
		sandwich_toppings.append(topping)
		print(topping, "added to sandwich...")
	print("Your sandwich is ready!\n")

add_sandwich_toppings("cheese", "turkey", "ham", "lettuce")
add_sandwich_toppings("tuna", "mayo", "pickles")
add_sandwich_toppings("bacon", "lettuce", "tomato")
'''
########################################################################
'''
def build_profile(first, last, **misc):
	profile = {}
	profile["first_name"] = first
	profile["last_name"] = last
	for key, value in misc.items():
		profile[key] = value
	return profile
	
user_profile = build_profile("christian", "gentry",
							school = "uta",
							major = "architecture", 
							gpa = 3.75)
print(user_profile)
'''
########################################################################

def car_info(manufacturer, model, **misc):
	car = {}
	car["manufacturer"] = manufacturer
	car["model"] = model
	for key, value in misc.items():
		car[key] = value
	return car
	
car1 = car_info("toyota", "corolla",
				color = "silver",
				year = "2005",
				miles = "175,000",
				previous_owner = "james gentry",
				current_owner = "christian gentry",
				plate_number = "cr8m158") 
print(car1)
	






