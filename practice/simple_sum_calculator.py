def SimpleAdding(num): 
    
    num = int(num)
    num_list = []
    
    while num > 0:
        num_list.append(num)
        num = num - 1
    
    num = sum(num_list)
    
    return num

#Execute
print("Simple addition calculator!\nex. 4: 1+2+3+4 = 10")    
print(SimpleAdding(input("Enter an integer value: ")))
