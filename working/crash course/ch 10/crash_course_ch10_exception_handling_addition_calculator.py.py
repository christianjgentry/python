while True:
	
	try:
		number1 = float(input("Please enter your first number: "))
		number2 = float(input("Please enter your second number: "))

	except ValueError:
		print("Your input must be a number!")
	
	else:
		add_numbers = number1 + number2
		print(str(number1) + " + " + str(number2) + " = " + str(add_numbers))
		break
