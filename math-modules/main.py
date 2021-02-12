# calculate's main module 
# DO NOT alter this module 
# Note from Bethany -- THIS CODE WAS WRITTEN BY MY PROFESSOR, DR. ELHAM EBRAHIMI,
# TO TEST OUR CODE. The only change I've made is this comment and line 7 where I 
# changed 'import lab15' to 'import calculate'.


import calculate
import random
import math

def main():
    print(format("main", "-^40"))

    ########################  call to function floor  ########################
    print(format("floor", "-^40"))
    try:
        x = random.uniform(1.0,10.0)
        print("value is {}.".format(x))
        print("floor value using math module: {}".format(math.floor(x)))
        print("floor value using lab15 module: {}".format(lab15.floor(x)))
    except:
        print("function 'floor' is not defined or something is wrong in the function")

    ########################  call to function ceil  ########################
    print(format("ceil", "-^40"))
    try: 
        x = random.uniform(1.0,10.0)
        print("test1: value is {}.".format(x))
        print("ceil value using math module: {}".format(math.ceil(x)))
        print("ceil value using lab15 module: {}".format(lab15.ceil(x)))
    except:
        print("function 'ceil' is not defined or something is wrong in the function")

    try: 
        x = random.randint(1,10)
        print("test2: value is {}.".format(x))
        print("ceil value using math module: {}".format(math.ceil(x)))
        print("ceil value using lab15 module: {}".format(lab15.ceil(x)))
    except:
        print("function 'ceil' is not defined or something is wrong in the function")

    
    ########################  call to function minVal  ########################
    print(format("minVal", "-^40"))
    
    try: 
        numList = list(range(random.randint(1,5), random.randint(5,10)))
        random.shuffle(numList)
        
        print("list is {}.".format(numList))
        print("min value using math module: {}".format(min(numList)))
        print("min value using lab15 module: {}".format(lab15.minVal(numList)))
    except:
        print("function 'minVal' is not defined or something is wrong in the function")
    

    ########################  call to function maxVal  ########################
    print(format("maxVal", "-^40"))
        
    try:
        numList = list(range(random.randint(1,5), random.randint(5,10)))
        random.shuffle(numList)
        
        print("list is {}.".format(numList))
        print("max value using math module: {}".format(max(numList)))
        print("max value using lab15 module: {}".format(lab15.maxVal(numList)))
    except:
        print("function 'maxVal' is not defined or something is wrong in the function")

    ########################  call to function total  ########################
    print(format("total", "-^40"))
        
    try:
        numList = list(range(random.randint(1,5), random.randint(5,10)))
        random.shuffle(numList)
        
        print("list is {}.".format(numList))
        print("sum value using math module: {}".format(sum(numList)))
        print("sum value using lab15 module: {}".format(lab15.total(numList)))
    except:
        print("function 'total' is not defined or something is wrong in the function")


    ########################  call to function mean  ########################
    print(format("total", "-^40"))
        
    try:
        numList = list(range(random.randint(1,5), random.randint(5,10)))
        random.shuffle(numList)
        
        print("list is {}.".format(numList))
        print("mean value using math module: {}".format(sum(numList)/len(numList)))
        print("mean value using lab15 module: {}".format(lab15.mean(numList)))
    except:
        print("function 'mean' is not defined or something is wrong in the function")

    ########################  call to function median  ########################
    print(format("median", "-^40"))
        
    try:
        numList = list(range(random.randint(1,5), random.randint(5,10)))
        random.shuffle(numList)
        
        print("list is {}.".format(numList))
        print("median value using lab15 module: {}".format(lab15.median(numList)))
    except:
        print("function 'median' is not defined or something is wrong in the function")

    ########################  call to function gcd  ########################
    print(format("gcd", "-^40"))
        
    try:
        num1 = random.randint(1,5)
        num2 = random.randint(5,10)
        
        print("the two values are {} and {}.".format(num1, num2))
        print("gcd value using math module: {}".format(math.gcd(num1, num2)))
        print("gcd value using lab15 module: {}".format(lab15.gcd(num1, num2)))
    except:
        print("function 'gcd' is not defined or something is wrong in the function")


main()













