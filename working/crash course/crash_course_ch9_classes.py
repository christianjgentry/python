########################################################################
'''
class Restaurant():
	#a simple attempt to model a restaurant.
	
	def __init__(self, name, cuisine):
		#initilize name and food type attributes.
		self.name = name
		self.cuisine = cuisine
		
	def describe_restaurant(self):
		#gives name of restaurant and the type of food they serve.
		print("The restaurant is called,", self.name + ".",
			"They serve", self.cuisine, "food.")
	
	def is_open(self):
		#opens the restaurant.
		print(self.name, "is now open!")

foodplace1 = Restaurant("Taco Bell", "Tex-Mex")
foodplace2 = Restaurant("Olive Garden", "Italian")
foodplace3 = Restaurant("Texas Road House", "Texan")

foodplace1.describe_restaurant()
foodplace1.is_open()
foodplace2.describe_restaurant()
foodplace2.is_open()
foodplace3.describe_restaurant()
foodplace3.is_open()
'''
########################################################################

class User():
	def __init__(self, first_name, last_name):
		#creates a basic instance of a user.
		self.first_name = first_name
		self.last_name = last_name
	
	def describe_user(self):
		#describes the modeled user instance.
		print("first name:", self.first_name.title())
		print("last name:", self.last_name.title())
	
	def greet_user(self):
		#greets the user.
		print("Greetings,", self.first_name.title() + "!")
		
user1 = User("christian", "gentry")
user2 = User("zachery", "gentry")
user3 = User("chantel", "garcia")

user1.greet_user()
user1.describe_user()

user2.greet_user()
user2.describe_user()

user3.greet_user()
user3.describe_user()

########################################################################
