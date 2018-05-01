'''
Created on Apr 17, 2018

@author: Samantha Hangsan
Assignment: 2

SPECS: 
- Prompt the user to enter 5 numbers
    - numbers must be entered as a comma separated list ( e.g. 4, 5, -2, 3, 7). 
- Calculate and output the average, the largest, and smallest the user entered. 
- Determine if the numbers are entered in ascending, descending order, or out of order.  
- Define the functions listed below in your program. 
	getAverage()
	getLargest()
	getSmallest()
	isOrdered()
'''
# FUNCTIONS
def getAverage(total, count):
	mean = float(total) / count
	return mean

def getLargest(list):
	num_max = (max(list)) 
	return num_max

def getSmallest(list):
	num_min = (min(list))
	return num_min

def isOrdered(list):
	if (sorted(list) == list):
		print('The numbers have been entered in ascending order.')
	elif(sorted(list, reverse = True) == list):
		print('The numbers have been entered in descending order.')
	else: 
		print('The numbers have been entered out of order.')

# PROGRAM
num_input = input('Enter 5 numbers separated by commas: ')
num_list = list(int(num) for num in num_input.split(','))

# check for 5 numbers
correct_num = False
while correct_num == False:
	total = 0
	for counter, user_input in enumerate(num_list,1):
		total += user_input
	if (counter) % 5 == 0:
		correct_num = True
	else:
		num_input = input('Invalid input! Please enter 5 numbers separated by commas: ')
		num_list = list(int(num) for num in num_input.split(','))
		correct_num = False

print('Your input was: ' + str(num_list))
print('The average of your 5 numbers is: ' + str(getAverage(total, counter)))
print('The largest value of your 5 numbers is: ' + str(getLargest(num_list)))
print('The smallest value of your 5 numbers is: ' + str(getSmallest(num_list)))
isOrdered(num_list)
