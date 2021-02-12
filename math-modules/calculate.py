# Bethany Fannin
# 10/25/2020
# CSC 131
# Lab 15 - renamed to Calculate to give more context
#
# Purpose: Practice modular program design by creating basic math functions
# and importing them into a main.py file
#
# Variables: num, lst, item, var, total, a, b, m, n, r
#


def floor(num):
    '''
    Takes one numeric value and
    rounds that number down to the
    closest integer value and
    returns it
    '''
    return int(num)

def ceil(num):
    '''
    Takes one numeric value, rounds up
    the number to the next integer value
    and then returns it. If the value is a float
    type but the decimal point is zero, then
    the integer version of the same value is
    returned.
    '''
    if num == int(num):
        return num
    else:
        return int(num + 1)


def minVal(lst):
    '''
    Takes a list of numbers and returns
    the smallest value from the list
    '''
    var = lst[0]
    for item in lst:
        if item < var:
            var = item
    return var


def maxVal(lst):
    '''
    Takes a list of numbers and returns
    the largest value from the list
    '''
    var = lst[0]
    for item in lst:
        if item > var:
            var = item
    return var

def total(lst):
    '''
    Takes a list of numbers and returns the total
    of the values within the list
    '''
    total = 0
    for item in lst:
        total = total + item
    return total

def mean(lst):
    '''
    Takes a list of numbers and returns
    the mean value. For example, if you pass
    1, 2, 3, then the result value should be
    2.
    '''
    return total(lst) / len(lst)

def median(lst):
    '''
    Takes a list of numbers, sorts it in order
    from highest to lowest, and returns
    the middle value
    '''
    lst.sort()

    if len(lst) % 2 == 0: # even
        a = len(lst)//2
        b = len(lst)//2 - 1
        return (lst[a] + lst[b]) / 2
    else: # odd
        return lst[len(lst)//2]

def gcd(num1, num2):
    '''
    Take two integers and returns
    the greatest common denominator of
    the two given values
    '''
    if num1 > num2:
        m = num1
        n = num2
    else:
        n = num1
        m = num2
    r = m % n
    while r != 0:
        m = n
        n = r
        r = m % n
    return n


    








    
