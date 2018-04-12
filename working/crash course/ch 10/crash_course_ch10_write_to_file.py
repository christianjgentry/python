filename = "guestbook.txt"

print("Welcome to my website!\nWould you please sign my guestbook?\n")

flag = True

while flag == True:
	
	guest_signature = input("Please enter your first and last name."
		+ "\nYou may type 'quit' to quit at any time: ")
		
	if guest_signature == "quit":
		flag = False
	else:
		with open(filename, 'a') as file_object:
			file_object.write(str(guest_signature + "\n"))
			
		print("Hello,", guest_signature + "!")
		
		guest_input = input("Could you please tell me what you like about programming?\n")
			
		if guest_input != "quit":
			with open(filename, 'a') as file_object:
				file_object.write(str(guest_signature + ": " + guest_input + "\n"))
		else:
			break
print("\nThanks for coming!")
		
