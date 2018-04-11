from random import randint

count = 0
number_list = []

while count < 10:
	count += 1
	d20 = randint(1,20)
	print(d20)
	number_list.append(d20)

print(number_list)
