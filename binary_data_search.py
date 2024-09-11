#!/usr/bin/env python3
# binary_data_search.py - Binary search for an item in an ordered list.

items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]


def binarySearch(item, itemlist):
    # Get the list size.
    listsize = len(itemlist) - 1
    # Start at the two ends of the list.
    lowerIdx = 0
    upperIdx = listsize

    while lowerIdx <= upperIdx:
        #  Calculate the middle point.
        midPt = (lowerIdx + upperIdx) // 2

        #  If item is found, return the index.
        if itemlist[midPt] == item:
            return midPt

        #  Otherwise, get the next midpoint.
        if item > itemlist[midPt]:
            lowerIdx = midPt + 1
        else:
            upperIdx = midPt - 1

    if lowerIdx > upperIdx:
        return None


# Search for an item in the items list with test values.
print(binarySearch(23, items))
print(binarySearch(87, items))
print(binarySearch(250, items))
