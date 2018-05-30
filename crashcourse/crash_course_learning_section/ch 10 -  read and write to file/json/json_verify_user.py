import json

def get_new_username():
	#prompt user for username.
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	return username
	
	
def get_stored_username():
	#retrieve previously stored username.
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return none
	else:
		return username


def greet_user():
	#Greet the user with the stored username.
	username = get_stored_username()
	if username:
		print("Welcome back,", username.title() + "!")
	else:
		username = get_new_username()
		print("We'll remember you when you come back", username.title() + "!")
		

def verify_user():
	#verifies if user logging in is same as last user.
	filename = 'username.json'
	try:
		username = get_stored_username()
		print("Hello, are you still User:", username + "?")
		if username:
			while True:
				confirm = input("yes/no: ")
				if confirm == "yes":
					greet_user()
					break
				elif confirm == "no":
					print(username, "has been logged out.")
					get_new_username()
					greet_user()
					break
				else: print("please enter either yes or no")
		else:
			get_new_username()
			greet_user()
	except:
		get_new_username()
		greet_user()
	

verify_user()



