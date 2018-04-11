#rpg module
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
