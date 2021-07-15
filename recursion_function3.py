#!/usr/bin/env python3
# recursion_function3.py

# Using recursion to implement power and factorial functions.

def power(num, power):
    if power == 0:
        return 1
    else:
        return num * power(num, power - 1)

# !5 = 5x4x3x2x1 = 120
def factorial(num):
    pass


print("{} to the power of {} is {}".format(5, 3, power(5, 3)))
print("{} to the power of {} is {}".format(1, 5, power(1, 5)))
print("{}! is {}".format(4, factorial(4)))
print("{}! is {}".format(0, factorial(0)))

