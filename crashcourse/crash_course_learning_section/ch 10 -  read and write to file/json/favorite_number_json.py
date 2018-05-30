import json

def get_favorite_number():
	#prompt user for username.
	favorite_number = input("What is your favorite number? ")
	filename = 'favoritenumber.json'
	with open(filename, 'w') as f_obj:
		json.dump(favorite_number, f_obj)
	return favorite_number
	
	
def get_stored_number():
	#retrieve previously stored username.
	filename = 'favoritenumber.json'
	try:
		with open(filename) as f_obj:
			favorite_number = json.load(f_obj)
	except FileNotFoundError:
		return none
	else:
		return favorite_number


def greet_user():
	favorite_number = get_stored_number()
	if favorite_number:
		print("Your favorite number is", favorite_number + "!")
	else:
		username = get_favorite_number()
		print("We will remember your favorite number,", favorite_number + "!")
		
		

get_favorite_number()
greet_user()


