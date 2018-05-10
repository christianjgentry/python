numbers = range(2000, 3201)

for number in numbers:
	if number % 7 == 0 and number % 5 != 0:
		print(number)
