#!/usr/bin/env python3
# linear_data_search.py - Linear search for an item in an unordered list.


# Declare a list of items to operate on.
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def findItem(item, itemList):
    for i in range(0, len(itemList)):
        if item == itemList[i]:
            return i

    return None


print(findItem(87, items))
print(findItem(250, items))
