def LongestWord(sen):
	#This function returns the longest word from a string.
	#If there are multiple words with the same length, the first is returned.
	 
	#container variables created
	word_lengths = []
	same_length = []
	
	#length of words in string added to word_lengths
	for item in sen.split():
		word = len(item)
		word_lengths.append(word)
	
	#the longest word length is stored as an int.
	longest_word = sorted(word_lengths)[-1]

	#words that match the longest length are extracted.
	flag = True
	while flag == True:
		for item in sen.split():
			if len(item) == longest_word:
				same_length.append(item)
				flag = False
	
	#The first longest word is assigned to a variable.			
	sen = same_length[0]
	return sen
		
#Execute
print(LongestWord(input()))


#Example: I went to the movies yesterday and I will go to the movies again tomorrow


