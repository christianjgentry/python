filename = 'learning_python.txt'

with open(filename) as file_object:
	lines = file_object.readlines()
	

message = []
for line in lines:
	print(line.rstrip())
	
print("\n_______________________________________\n")	


for line in lines:
	print(str(line.rstrip()).replace("Python", "C"))


	
