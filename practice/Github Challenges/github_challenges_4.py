'''
Question 4
Level 1

Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
'''
numbers = "34,67,55,33,12,98"

num_list = numbers.split(',')
num_tuple = tuple(num_list)
print(num_list, num_tuple)

