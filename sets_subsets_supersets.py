#!/usr/bin/env python3
# sets_subsets_supersets.py

# Set comparision.
if {1, 3, 5} == {5, 3, 1}:
    print("{1, 3, 5} is equal to {5, 3, 1}")
else:
    print("{1, 3, 5} is not equal to {5, 3, 1}")

if {1, 3, 5} != {5, 3, 1}:
    print("{1, 3, 5} is not equal to {5, 3, 1}")
else:
    print("{1, 3, 5} is equal to {5, 3, 1}")


# Subset and superset
if {1, 3}.issubset({1, 3, 4}) == True:
    print("{1, 3} is a subset of {1, 3, 4}")
else:
    print("{1, 3} is not a subset of {1, 3, 4}")

if {1, 3, 5, 7}.issuperset({1, 3, 5}) == True:
    print("{1, 3, 5, 7} is a superset of {1, 3, 5}")
else:
    print("{1, 3, 5, 7} is not a superset of {1, 3, 5}")
