#!/usr/bin/env python3

# Demonstrate using the random module to generate random numbers.

import random


# print(random.random())
# print(random.random())
# print(random.random())

# TODO: Implement a coin toss function. 
for i in range(10):
    if (random.random() <= 0.5):
        print("Heads")
    else:
        print("Tails")

# TODO: Get a random number within a given range.
print(random.uniform(1, 100))

# TODO: Generate random integers within a given range.
print(random.randint(1, 100))

# TODO: Generate random integers with a step function
# this example chooses from 0 to 100 with a step of 5.
print(random.randrange(0, 100, 5))

# TODO: Use the seed function to position the random number generator.
random.seed(1)
print(random.random())
print(random.random())
print("---------------")

random.seed(1)
print(random.random())
print(random.random())

