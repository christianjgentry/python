def alpha_sort(string):
	#sorts letters in string by alphabetical order.
	string = sorted(string)
	string = "".join(string)
	
	return string

#Execute
print(alpha_sort("hello"))
