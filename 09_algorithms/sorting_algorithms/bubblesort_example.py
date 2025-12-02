#!/usr/bin/env python3
"""bubblesort_example.py - Implementation of the Bubble Sort algorithm.

Bubble Sort is a simple comparison-based sorting algorithm that:
1. Compares adjacent elements
2. Swaps them if they're in wrong order
3. Repeats until the array is sorted

Algorithm Characteristics:
- Time Complexity:
  * Best case: O(n) - when already sorted (with optimization)
  * Average case: O(n²)
  * Worst case: O(n²)
- Space Complexity: O(1) - sorts in-place
- Stable: Preserves order of equal elements
- Simple but inefficient for large datasets

How it works:
- In each pass, the largest unsorted element "bubbles up" to its position
- After i passes, the last i elements are in their final positions
- The name comes from smaller elements "bubbling" to the top
"""


def bubbleSort(dataset):
    """Sort an array using the Bubble Sort algorithm.
    
    This implementation sorts the array in-place by repeatedly
    comparing and swapping adjacent elements.
    
    Args:
        dataset (list): The array to sort (modified in-place)
    
    Algorithm:
        - Outer loop: determines the range to sort (decreases each pass)
        - Inner loop: compares adjacent elements and swaps if needed
        - After each outer loop iteration, one more element is in place
    
    Example:
        [5, 2, 8, 1] -> [2, 5, 1, 8] -> [2, 1, 5, 8] -> [1, 2, 5, 8]
    """
    # Start with the array length and decrement each time
    # Range: len-1 down to 1 (because index 0 will be sorted last)
    for i in range(len(dataset) - 1, 0, -1):
        # Inner loop: compare adjacent elements up to position i
        # Elements after i are already sorted from previous passes
        for j in range(i):
            # If current element is greater than next, swap them
            if dataset[j] > dataset[j + 1]:
                # Swap using temporary variable
                temp = dataset[j]
                dataset[j] = dataset[j + 1]
                dataset[j + 1] = temp
        
        # Show progress after each pass
        print("Current state: ", dataset)


def main():
    """Main function to demonstrate Bubble Sort."""
    # Create an unsorted list
    list1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    
    print("Original list:", list1)
    print("\nSorting process:")
    
    # Sort the list (modifies in-place)
    bubbleSort(list1)
    
    # Display final result
    print("\nFinal Result: ", list1)


if __name__ == "__main__":
    main()
