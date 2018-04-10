'''
alien_0 = {}
alien_0["color"] = "green"
alien_0["points"] = 5
alien_0["name"] = "Kl'iixzuhl"

print(alien_0)
print(alien_0["color"])

del alien_0["color"]

print(alien_0)

for item in alien_0:
	print(item)

########################################################################

person_1 = {
	"first" : "chantel",
	"last" : "garcia",
	"age" : 23,
	"eyecolor" : "honey",
	"hometown" : "monahans",
	"college" : "uta",
	"gender" : "female",
		}
		
print(person_1)

print(person_1["eyecolor"])

favorite_numbers = {
	"chantel" : "64",
	"christian" : "74",
	"zachery" : "75",
	"jj" : "66",
	"mocha" : "4",
	}
	
print(favorite_numbers)

print("Mocha's favorite number is", favorite_numbers["mocha"] + ".")

########################################################################

programming_dictionary = {
	"variable:" : " a container that holds value.",
	"dictionary:" : " a type of list that contains keys and values.",
	"concatenation:" : " the chaining of strings together using the + symbol.",
	"string:" : " an array of characters that are stored as text",
	"list:" : " a collection of elements",
	"set()" : "runs through list of values but only stores unique values.",
	"float" : "number values with decimal places",
	"integer" : "number values with no decimal places.",
	"while loop" : "loop that runs until either broken or until the value is no longer true."
	}

for key, value in programming_dictionary.items():
	print("Key: " + key + "\nValue: " + value + "\n")
	
rivers = {
	"egypt" : "nile",
	"mississippi" : "mississippi river",
	"texas" : "rio grande",
		 	}
print(rivers)

for location, river in rivers.items():
	print("The", river, "runs through", location)

for key in rivers.keys():
	print(key)

for value in rivers.values():
	print(value)

########################################################################

favorite_languages = {
	"christian" : "python",
	"zachery" : "c#",
	"john" : "python",
	"matt" : "java",
	"jason" : "",
	"carol" : "c",
	"amy" : "python",
	"justin" : "c#",
	"alex" : "",
	"brandon" : "",
	}

coders = ["christian", "alec", "tanner", "zachery", "brandon", "james"]

for coder in coders:
	if coder in favorite_languages.keys():
		print(coder, "thank you for taking my survey!")
	else:
		print(coder, "please take my survey")


for name, language in favorite_languages.items():
	
	if len(language) == 0:
		print(name, ". You still need to take the survey!")
	elif len(language) > 0:
		print(name, ". Thank you for taking my survey!")
		
########################################################################
'''

names = {

"christian" : {
	"first" : "christian",
	"last" : "gentry",
	"city" : "stephenville",
	},
	
"chantel" : {
	"first" : "chantel",
	"last" : "garcia",
	"city" : "monahans",
	},

"zachery" : {
	"first" : "zachery",
	"last" : "gentry",
	"city" : "stephenville",
	},
	}

for name, info in names.items():
	print("This is", info["first"], info["last"] +".\n" + info["first"], "lives in", info["city"])
	
########################################################################


pet = {
	"name" : "",
	"owner" : "",
}










