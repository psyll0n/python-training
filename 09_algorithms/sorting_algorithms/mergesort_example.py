#!/usr/bin/env python3
# mergesort_example.py - Demonstates the merge sort algorithm.

items = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8, 0, 56, 23, 11]


def mergeSort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]

        #  Recursively break down the arrays.
        mergeSort(leftarr)
        mergeSort(rightarr)

        #  Now perform the merging operations.
        i = 0  # index into the left array
        j = 0  # index into the right array
        k = 0  # index into merged array

        #  While both arrays have content.
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i += 1
            else:
                dataset[k] = rightarr[j]
                j += 1
            k += 1

        #  If the left array still has values, add them.
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += 1
            k += 1

        #  If the right array still has values, add them.

        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j += 1
            k += 1


# Test the merge sort algorithm with data.
print(items)
mergeSort(items)
print(items)
