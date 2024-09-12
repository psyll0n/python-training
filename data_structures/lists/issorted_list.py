#!/usr/bin/env python3
# issorted_list.py - Determine if a list is sorted.


items1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
items2 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def isSorted(itemslist):
    # Using the brute force method.
    # for i in range(0, len(itemslist)-1):
    #     if itemslist[i] > itemslist[i+1]:
    #         return False

    return all(itemslist[i] <= itemslist[i + 1] for i in range(0, len(itemslist) - 1))

    # return True


print(isSorted(items1))
print(isSorted(items2))
