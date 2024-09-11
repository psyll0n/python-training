#!/usr/bin/env python3
# find_max_value.py - Use a recursive algorithm to find the maximum value in a list.

# Declare a list of values to operate on.
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def findMax(items):
    # Breaking condition: last item in list? Return it.
    if len(items) == 1:
        return items[0]

    # Otherwise get the first item and call function again
    # to operate on the rest of the list.
    op1 = items[0]
    print(op1)
    op2 = findMax(items[1:])
    print(op2)

    # Perform the comparison when we are down to just two.
    if op1 > op2:
        return op1
    else:
        return op2


# Test the function.
print(findMax(items))
