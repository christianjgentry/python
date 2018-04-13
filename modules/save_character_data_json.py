import json

class Character():
	#base class
	def __init__(self, dictionary):
		for key, value in dictionary.items():
			setattr(self, key, value)
			
			
def store_character_data(name, hp, atk):
	#stores entered character data into a json as a dictionary.
	filename = 'character_data.json'
	with open(filename, 'w') as f_obj:
		character_data = {
					"name" : name,
					"hp" : hp,
					"atk" : atk,
					}
		json.dump(character_data, f_obj)


def get_character_data():
	#gets stored character data from json.
	filename = 'character_data.json'
	with open(filename, 'r') as f_obj:
		character_data = json.load(f_obj)
		return(character_data)


store_character_data("Christian", 150, 14)

player1 = Character(get_character_data())
player1_variables = vars(player1)

print(player1_variables)
print(player1.name)
print(player1.hp)
print(player1.atk)





