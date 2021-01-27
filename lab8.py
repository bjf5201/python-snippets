# Bethany Fannin
# Date: 09/14/2020
# CSC 131-007 - Lab 8
# Purpose - Practicing with

# Variables - num, total, positive, negative


###### Problem 1: Practice while statements,
######          print out total of all even numbers between 100 and 200, inclusive
num = 100
total = 0

while num <= 200:
    total = total + num
    num = num + 2

print('{:.^90s}'.format('Problem 1 - Practicing While Loop'))
print('{:.^90s}'.format('Adding up even numbers between 100 and 200, inclusive'))
print('The total value equals to', total)
print('\n')

###### Probelm 2: Practice while statements to sum up values
######          Print out the sum of a series of integers entered by user,
######          if user wants to quit program, they enter a "-1"

print('{:.^90s}'.format('Problem 2 - Summing values entered by the user'))

total = 0
num = int(input('Enter a number (-1 to quit): '))

while num != -1:
    total = total + num
    num = int(input('Enter a number (-1 to quit): '))

print('The sum is:', total);
print('\n')

###### Problem 3: Practice using while statements with controls
######          Sum a series of positive integers entered by user, except those
######          that are greater than 100. If user wants to quit, they enter "-1"

print('{:90s}'.format('Problem 3 - Summing positive values entered by the user that are less than 100'))
print('{:90s}'.format('Summing positive values entered by the user that are less than 100!'))

total = 0
num = int(input('Please enter first number to sum (enter -1 to quit): '))

while num != -1:
    if num < 0 or num >= 100:
        num = int(input('Please enter next number (enter -1 to quit): '))
    else:
        total = total + num
        num = int(input('Please enter next number (enter -1 to quit): '))

print('The sum of all the positive values less than 100 is:', total)

###### Problem 4: Practice using while loop with controls
######          Sum a series of integers (both positive and negative) that user
######          enters and count number of positive and negative integers entered
######          and display to user. To quit, user can enter "q"

print('{:90s}'.format('Problem 4 - Practicing While Loop'))
print('{:90s}'.format('Counting the number of positive and negative values entered by the user!'))

positive = 0
negative = 0
num = input('Please enter first number (enter "q" to quit): ')

while num != 'q':
    if int(num) < 0:
        negative = negative + 1
        num = input('Please enter next number (enter "q" to quit): ')
    elif int(num) >= 0:
        positive = positive + 1
        num = input('Please enter next number (enter "q" to quit): ')

print('Number of positive values entered: ', positive)
print('Number of negative values entered: ', negative)
    
