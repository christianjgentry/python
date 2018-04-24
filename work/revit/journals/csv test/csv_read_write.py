import csv

filename = 'users_test.csv'

'''
with open(filename, 'r') as csv_file:
	csv_reader = csv.reader(csv_file)
	
	next(csv_reader)
	
	for line in csv_reader:
		print(line)
'''

with open(filename, 'r') as csv_file:
	csv_reader = csv.reader(csv_file)
		
	with open('test_write_csv', 'w') as new_file:
		csv_writer = csv.writer(new_file, delimiter=',')
	
		for line in csv_reader:
			csv_writer.writerow(line)
		


