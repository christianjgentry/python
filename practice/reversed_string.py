def FirstReverse(string): 
	reverse = []
	string = list(string)

	while len(string) > 0:
		reverse.append(string[-1])
		string.pop()
	
	reverse = ''.join(reverse)

	return reverse

# keep this function call here  
#print(FirstReverse(input("Type out a sentence or word to see it reversed!: ")))



text = "abcdefg"

print(text)


print(text[::-1])
