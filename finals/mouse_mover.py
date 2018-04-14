mouse_moves = []

while True:

	try:
		x_moves = int(input("How many times should the mouse move?: "))	
		break
	except ValueError:
		print("\nYou must enter an integer!\n")

x_moves = abs(x_moves)
x_count = 1

print("\nThe mouse will make", str(x_moves), "moves.\n")

while x_count <= x_moves:
	valid_inputs = ["up", "down", "left", "right"]
	user_input = input("Where should the mouse move?\n" + str(valid_inputs) +": ")
	user_input = user_input.lower()
	
	if user_input in valid_inputs:
		x_count += 1
		mouse_moves.append(user_input)
	else:
		print("invalid move! Please try again.\n")

print("\nThe mouse will move")
for move in mouse_moves:
	print(move.title())

