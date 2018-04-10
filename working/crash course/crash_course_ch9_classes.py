########################################################################
'''
class Restaurant():
	#a simple attempt to model a restaurant.
	
	def __init__(self, name, cuisine):
		#initilize name and food type attributes.
		self.name = name
		self.cuisine = cuisine
		self.number_served = 0
		
	def describe_restaurant(self):
		#gives name of restaurant and the type of food they serve.
		print("The restaurant is called,", self.name + ".",
			"They serve", self.cuisine, "food.")
	
	def is_open(self):
		#opens the restaurant.
		print(self.name, "is now open!")
	
	def increment_number_served(self, customers):
		#adds customers to total number served.
		if customers > 0:
			self.number_served = self.number_served + customers
		else:
			print("You cannot enter a negative number of customers!")

foodplace1 = Restaurant("Taco Bell", "Tex-Mex")
foodplace2 = Restaurant("Olive Garden", "Italian")
foodplace3 = Restaurant("Texas Road House", "Texan")

restaurant = Restaurant("christian's grill", "bbq")

print(restaurant.number_served)
restaurant.number_served = 74
print(restaurant.number_served)

restaurant.increment_number_served(39)
print(restaurant.number_served)
'''
########################################################################

class User():
	def __init__(self, first_name, last_name):
		#creates a basic instance of a user.
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = 0
	
	def describe_user(self):
		#describes the modeled user instance.
		print("first name:", self.first_name.title())
		print("last name:", self.last_name.title())
	
	def greet_user(self):
		#greets the user.
		print("Greetings,", self.first_name.title() + "!")
		
	def increment_login_attempts(self):
		self.login_attempts += 1
		print(self.first_name.title() + ":\n" + 
			"Login Attempts:", self.login_attempts)
		
	def reset_login_attempts(self):
		self.login_attempts = 0
		print("Login Attempts Reset!\n" + 
			self.first_name.title() + ":\n" + 
			"Login Attempts:", self.login_attempts)
		
		
user1 = User("christian", "gentry")
user2 = User("zachery", "gentry")
user3 = User("chantel", "garcia")

user1.greet_user()
user1.describe_user()

user2.greet_user()
user2.describe_user()

user3.greet_user()
user3.describe_user()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()


########################################################################
'''
class Character():
	#Creates a base framework for a game character.
	
	def __init__(self, name, hp=100, atk=12):
		#Character is initialized with base attributes.
		self.name = name
		self.hp_max = hp
		self.hp_current = hp
		self.atk = atk
		
		
	def heal_self(self):
		#Character heals self for 40% of maximum health.
		heal_self = int(self.hp_max * 0.4)
		self.hp_current = self.hp_current + heal_self
		if self.hp_current > self.hp_max:
			self.hp_current = self.hp_max
		print(self.name.title(), "was healed for", heal_self, "hp!")
	
	def atk_basic(self, target):
		#A basic attack that deals atk value to target's hp value.
		target.hp_current = target.hp_current - self.atk
		print(self.name.title(), "dealt", self.atk,
			"damage to", target.name + "!")
		

def brawl(character_1, character_2):
	#Two characters fight to the death.
	while True:
		character_1.atk_basic(character_2)
		character_2.atk_basic(character_1)
		
		if character_1.hp_current <= 0:
			print(character_2.name.title(), "wins the brawl!")
			break
		if character_2.hp_current <= 0:
			print(character_1.name.title(), "wins the brawl!")
			break


christian = Character("christian", atk=16)
zachery = Character("zachery", hp=150)

print(zachery.hp_current)
christian.atk_basic(zachery)
christian.atk_basic(zachery)
christian.atk_basic(zachery)
christian.atk_basic(zachery)
print(zachery.hp_current)

zachery.heal_self()
zachery.heal_self()
zachery.heal_self()

print(zachery.hp_current)

brawl(christian, zachery)
'''
########################################################################

		

















