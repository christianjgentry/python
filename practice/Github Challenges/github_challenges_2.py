'''
Question 2
Level 1

Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
'''

def FirstFactorial(num):
	#calculate the factorial value of an integer. 
    num = int(num)
    factorial = num
    
    while num > 1:
        factorial = factorial * (num - 1)
        num = num - 1
      
    return factorial
    
    
# Execute
print(FirstFactorial(input("Enter an integer value:")))






