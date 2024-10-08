# /usr/bin/env python3
# Functions for generating random data sequences.

import random
import string


# Use the choice function to generate a random element from a sequence.
moves = ["rock", "paper", "scissors"]
# print(random.choice(moves))

# Use the choices function to generate a list of random elements.
roulette_wheel = ["black", "red", "green"]
weights = [18, 18, 2]
print(random.choices(roulette_wheel, weights, k=10))

# The sample function randomly selects elements from a population.
# without replacement. (The chosen elements are not replaced.)
chosen = random.sample(string.ascii_uppercase, 5)
print(chosen)

# The shuffle function randomly shuffles a sequence in place.
players = ["Joe", "Bob", "Tom", "Dick", "Harry"]
random.shuffle(players)
print(players)

# To shuffle an immutable sequence, use the sample function first.
result = random.sample(string.ascii_uppercase, k=len(string.ascii_uppercase))
random.shuffle(result)
print("".join(result))
