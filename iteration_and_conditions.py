#!/usr/bin/env python3
# iteration_and_conditions.py - Using a for loop to iterate over the numbers 1 to 100...
# If - elif - else Conditional logic example

for i in range(1,101):
    if i % 100 == 0:
        print(f"{i} baz")
    elif i % 3 == 0:
        print(f"{i} foo")
    elif i % 5 == 0:
        print(f"{i} bar")
    else: 
        print(i)