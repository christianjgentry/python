def word_count(filename):
	#counts the words in a text document.
	try:
		with open(filename, 'r') as file_object:
			lines = file_object.read()
			split_lines = lines.split()
			word_count = []
			
			for line in split_lines:
				word_count.append(line)
				
			print("There are", len(word_count), "words in", filename)
			
	except FileNotFoundError:
		print("Oops, the specified file '", filename, "' cannot be found." +
			" Please check your filepath and try again.")


def word_occurence_dict(filename):
	'''creates a dictionary of all words in a text document with 
		corresponding occurence value.'''
	try:
		with open(filename, 'r') as file_object:
			lines = file_object.read().lower()
			split_lines = lines.split()
			non_repeating = []
			word_occurence = {}	
			
			for word in split_lines:
				if word not in non_repeating:
					non_repeating.append(word)
				else:
					pass
			
			for item in non_repeating:
				count = split_lines.count(item)
				word_occurence[item] = count
	except FileNotFoundError:
		print("Oops, the specified file '", filename, "' cannot be found." +
			" Please check your filepath and try again.")
	else:
		return word_occurence

