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
















  
