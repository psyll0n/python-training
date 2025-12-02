#!/usr/bin/env python3
"""quicksort_example.py - Implementation of the QuickSort algorithm.

QuickSort is a highly efficient, divide-and-conquer sorting algorithm that:
1. Selects a 'pivot' element from the array
2. Partitions the array around the pivot
3. Recursively sorts the sub-arrays

Algorithm Characteristics:
- Time Complexity:
  * Best case: O(n log n)
  * Average case: O(n log n)
  * Worst case: O(n²) - when pivot is always min/max
- Space Complexity: O(log n) - due to recursion stack
- Not stable (doesn't preserve order of equal elements)
- In-place sorting (modifies original array)

How it works:
1. Choose first element as pivot
2. Partition: move smaller elements left, larger right
3. Recursively apply to left and right partitions
4. Base case: arrays of size 0 or 1 are already sorted
"""

# Sample unsorted data
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53, 3, 75, 26, 2, 81]


def quickSort(dataset, first, last):
    """Sort an array using the QuickSort algorithm.
    
    This is the main recursive function that divides the array
    into partitions and sorts them.
    
    Args:
        dataset (list): The array to sort
        first (int): Starting index of the portion to sort
        last (int): Ending index of the portion to sort
    
    Note:
        Modifies dataset in-place. No return value.
    """
    if first < last:
        # Calculate the split point (pivot index after partitioning)
        pivotIdx = partition(dataset, first, last)

        # Recursively sort the left partition (elements < pivot)
        quickSort(dataset, first, pivotIdx - 1)
        
        # Recursively sort the right partition (elements > pivot)
        quickSort(dataset, pivotIdx + 1, last)


def partition(datavalues, first, last):
    """Partition the array around a pivot value.
    
    This function rearranges the array so that:
    - All elements smaller than pivot are to its left
    - All elements larger than pivot are to its right
    - Returns the final position of the pivot
    
    Args:
        datavalues (list): The array to partition
        first (int): Starting index of partition range
        last (int): Ending index of partition range
    
    Returns:
        int: The final index position of the pivot element
    
    Algorithm:
        1. Choose first element as pivot
        2. Use two pointers (lower, upper) moving towards each other
        3. Swap elements that are on wrong side of pivot
        4. When pointers cross, swap pivot to its final position
    """
    # Choose the first item as the pivot value
    pivotvalue = datavalues[first]
    
    # Establish the upper and lower indexes
    lower = first + 1  # Start after pivot
    upper = last       # Start at end

    # Start searching for the crossing point
    done = False
    while not done:
        # Advance the lower index while values are less than pivot
        while lower <= upper and datavalues[lower] <= pivotvalue:
            lower += 1

        # Advance the upper index while values are greater than pivot
        while datavalues[upper] >= pivotvalue and upper >= lower:
            upper -= 1

        # If the two indexes cross, we have found the split point
        if upper < lower:
            done = True
        else:
            # Swap the elements at lower and upper positions
            temp = datavalues[lower]
            datavalues[lower] = datavalues[upper]
            datavalues[upper] = temp

    # When the split point is found, exchange the pivot value
    # with the value at the upper index
    temp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = temp

    # Return the split point index (pivot's final position)
    return upper


# ===== Demo: Test QuickSort =====

print("Original array:")
print(items)

# Sort the array using QuickSort
quickSort(items, 0, len(items) - 1)

print("\nSorted array:")
print(items)
