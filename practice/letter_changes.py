'''
Challenge
Using the Python language, have the function LetterChanges(str) take the str
parameter being passed and modify it using the following algorithm. 
Replace every letter in the string with the letter following it in the alphabet
(ie. c becomes d, z becomes a). Then capitalize every vowel in this new string 
(a, e, i, o, u) and finally return this modified string. 
'''

def LetterChanges(user_input): 

    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    vowels = ["a", "e", "i", "o", "u"]
    
    user_input = user_input
    output = []
    
    for letter in user_input:
        if letter in letters and letter != "z":
            temp_char = letters[(int(letters.index(letter)) + 1)]
            output.append(temp_char)
        elif letter in letters and letter == "z":
            temp_char = letters[0]
            output.append(temp_char)
        else:
            output.append(letter)
            
    for letter in output:
        if letter in vowels:
            letter_upper = letter.upper()
            letter_index = output.index(letter)
            del output[output.index(letter)]
            output.insert(letter_index, letter_upper)
            
    output = ''.join(output)
    
    return output

print(LetterChanges("fun times!"))
    










  
