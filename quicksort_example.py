#!/usr/bin/env python3
# quicksort_algorithm.py - Demonstration of the quicksort algorithm.

items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53, 3, 75, 26, 2, 81]


def quickSort(dataset, first, last):
    if first < last:
        # Calculate the split point.
        pivotIdx = partition(dataset, first, last)

        # Now sort the two partitions.
        quickSort(dataset, first, pivotIdx - 1)
        quickSort(dataset, pivotIdx + 1, last)


def partition(datavalues, first, last):
    # Choose the first item as the pivot value.
    pivotvalue = datavalues[first]
    # Establish the upper and lower indexes.
    lower = first + 1
    upper = last

    # Start searching for the crossing point.
    done = False
    while not done:
        # TODO: Advance the lower index.
        while lower <= upper and datavalues[lower] <= pivotvalue:
            lower += 1

        # TODO: Advance the upper index.
        while datavalues[upper] >= pivotvalue and upper >= lower:
            upper -= 1

        # TODO: If the two indexes cross, we have found the split point.
        if upper < lower:
            done = True
        else:
            temp = datavalues[lower]
            datavalues[lower] = datavalues[upper]
            datavalues[upper] = temp

    # When the split point is found, exchange the pivot value.
    temp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = temp

    # Return the split point index.
    return upper


# Test the merge sort with data.
print(items)
quickSort(items, 0, len(items) - 1)
print(items)
