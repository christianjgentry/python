#find the third largest number in a list of numbers.
numbers = [0, 15, 1024, 1235, 6243, 1246, 6254, 2356, 2457, 4568,
	513245, 7345, 2346, 7534, 2345, 5234, 5234, 342, 2342, 6346, 6234]
	
sorted_numbers = sorted(numbers)

third_largest_number = sorted_numbers[-3]

print(third_largest_number)
