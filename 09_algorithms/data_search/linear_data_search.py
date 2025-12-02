#!/usr/bin/env python3
"""linear_data_search.py - Implementation of linear search algorithm.

Linear Search (Sequential Search) is the simplest search algorithm that:
1. Examines each element in sequence
2. Compares it with the target value
3. Returns the index if found, or None if not found

Algorithm Characteristics:
- Time Complexity:
  * Best case: O(1) - target is first element
  * Average case: O(n)
  * Worst case: O(n) - target is last or not present
- Space Complexity: O(1) - no extra space needed
- Works on unsorted data
- Simple but inefficient for large datasets

Use Cases:
- Small datasets
- Unsorted data
- Single search operations
- When data structure doesn't support faster searches
"""

# Declare a list of items to operate on (unsorted)
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def findItem(item, itemList):
    """Search for an item in a list using linear search.
    
    Sequentially checks each element in the list until the target
    item is found or the end of the list is reached.
    
    Args:
        item: The value to search for (can be any type)
        itemList (list): The list to search through
    
    Returns:
        int: The index position of the item if found
        None: If the item is not in the list
    
    Example:
        >>> findItem(87, [6, 20, 8, 19, 56, 23, 87, 41])
        6
        >>> findItem(99, [6, 20, 8, 19, 56, 23, 87, 41])
        None
    
    Time Complexity:
        O(n) - must potentially check every element
    """
    # Iterate through each index in the list
    for i in range(0, len(itemList)):
        # Check if current element matches target
        if item == itemList[i]:
            return i  # Found! Return the index
    
    # If loop completes without finding item, return None
    return None


# ===== Demo: Test linear search =====

print("Searching for 87 in", items)
result1 = findItem(87, items)
if result1 is not None:
    print(f"Found at index: {result1}")
else:
    print("Not found")

print("\nSearching for 250 in", items)
result2 = findItem(250, items)
if result2 is not None:
    print(f"Found at index: {result2}")
else:
    print("Not found")
