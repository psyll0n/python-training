# Algorithms

Algorithm implementations and data structure algorithms. This section covers sorting algorithms, search algorithms, and data structures.

## 📂 Contents

### [Sorting Algorithms](./sorting_algorithms/)
Various sorting algorithm implementations with complexity analysis.

#### Bubble Sort
- **bubblesort_example.py** - Simple comparison-based sorting
  - Repeatedly swaps adjacent elements
  - Time Complexity: O(n²) average and worst case, O(n) best case
  - Space Complexity: O(1) - sorts in-place
  - Stable sorting algorithm
  - Good for: Small datasets, educational purposes

**Algorithm:**
```
Compare adjacent elements and swap if in wrong order
Repeat until no swaps needed
Largest element "bubbles up" to the end each pass
```

---

#### Quick Sort
- **quicksort_example.py** - Divide-and-conquer sorting
  - Choose pivot, partition array around it
  - Recursively sort left and right partitions
  - Time Complexity: O(n log n) average, O(n²) worst case
  - Space Complexity: O(log n) - recursion stack
  - Not stable (doesn't preserve order of equal elements)
  - Good for: General purpose, large datasets

**Algorithm:**
```
1. Choose pivot element (first, last, random, or median)
2. Partition: move smaller elements left, larger right
3. Recursively sort left partition
4. Recursively sort right partition
5. Base case: arrays of size 0 or 1 are sorted
```

---

#### Merge Sort
- **mergesort_example.py** - Stable divide-and-conquer sorting
  - Divide array into halves recursively
  - Merge sorted halves
  - Time Complexity: O(n log n) all cases
  - Space Complexity: O(n) - requires auxiliary array
  - Stable sorting algorithm
  - Good for: Linked lists, guaranteed O(n log n), external sorting

**Algorithm:**
```
1. Divide array into two halves
2. Recursively sort each half
3. Merge two sorted halves into one sorted array
4. Base case: array of size 1 is sorted
```

---

#### Custom Sorting
- **sort_by_last_letter.py** - Custom sorting with key functions
  - Using Python's built-in sort() with custom key
  - Lambda functions for sorting criteria
  - Multiple sorting keys

---

### [Data Search](./data_search/)
Search algorithm implementations.

#### Linear Search
- **linear_data_search.py** - Sequential search algorithm
  - Check each element one by one
  - Time Complexity: O(n) worst case, O(1) best case
  - Space Complexity: O(1)
  - Works on unsorted data
  - Simple but inefficient for large datasets

**Algorithm:**
```
for each element in list:
    if element == target:
        return index
return None (not found)
```

**When to use:**
- Small datasets (< 100 elements)
- Unsorted data
- Single search operation
- Data structure doesn't support faster search

---

#### Find Maximum Value
- **find_max_value.py** - Finding the largest element
  - Single pass through array
  - Time Complexity: O(n)
  - Space Complexity: O(1)

---

#### Find Minimum Value
- **find_the_smallest_number.py** - Finding the smallest element
  - Single pass through array
  - Time Complexity: O(n)
  - Space Complexity: O(1)

---

### [Heap](./heap/)
Heap data structure implementation.

- Binary heap (max heap, min heap)
- Heapify operations
- Heap sort
- Priority queue implementation

**Properties:**
- Complete binary tree
- Parent >= children (max heap)
- Parent <= children (min heap)

**Operations:**
- Insert: O(log n)
- Extract max/min: O(log n)
- Peek: O(1)
- Heapify: O(n)

**Use Cases:**
- Priority queues
- Heap sort
- Finding kth largest/smallest
- Median maintenance

---

## 📊 Algorithm Comparison

### Sorting Algorithms

| Algorithm | Best Case | Average Case | Worst Case | Space | Stable |
|-----------|-----------|--------------|------------|-------|--------|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) | ✓ |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) | ✗ |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | ✓ |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) | ✗ |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | ✓ |
| **Python sort()** | O(n) | O(n log n) | O(n log n) | O(n) | ✓ |

### Search Algorithms

| Algorithm | Time Complexity | Space | Requires Sorted |
|-----------|----------------|-------|-----------------|
| **Linear Search** | O(n) | O(1) | No |
| **Binary Search** | O(log n) | O(1) | Yes |
| **Hash Table** | O(1) average | O(n) | No |

---

## 🎯 Learning Path

1. **Linear Search** - Understand basic searching
2. **Bubble Sort** - Learn sorting fundamentals
3. **Quick Sort** - Master divide-and-conquer
4. **Merge Sort** - Understand stable sorting
5. **Find Min/Max** - Simple optimization problems
6. **Heap** - Advanced data structure

## 💡 Tips

### Choosing a Sorting Algorithm

**Use Bubble Sort when:**
- Dataset is very small (< 10 elements)
- Teaching/learning sorting concepts
- Data is nearly sorted

**Use Quick Sort when:**
- Need fast average-case performance
- Memory is limited (in-place sorting)
- Data is random (not already sorted)

**Use Merge Sort when:**
- Need guaranteed O(n log n)
- Stability is required
- Sorting linked lists
- External sorting (disk-based)

**Use Python's built-in sort() when:**
- In production code (highly optimized Timsort)
- Need reliable performance
- Want stability

### Choosing a Search Algorithm

**Use Linear Search when:**
- Data is unsorted
- Small dataset (< 100)
- Single search operation

**Use Binary Search when:**
- Data is sorted
- Multiple searches needed
- Large dataset

**Use Hash Table when:**
- Need O(1) lookup
- Have enough memory
- Can handle collisions

## ⚡ Optimization Techniques

### 1. Early Exit
```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i  # Exit immediately when found
    return None
```

### 2. Sentinel Linear Search
```python
def sentinel_search(arr, target):
    last = arr[-1]
    arr[-1] = target
    i = 0
    while arr[i] != target:
        i += 1
    arr[-1] = last
    return i if i < len(arr) - 1 or last == target else None
```

### 3. Binary Search (Sorted Data)
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None
```

## 🧮 Complexity Analysis

### Time Complexity
- **O(1)** - Constant: Array access, hash table lookup
- **O(log n)** - Logarithmic: Binary search, balanced tree
- **O(n)** - Linear: Linear search, single pass
- **O(n log n)** - Linearithmic: Efficient sorting
- **O(n²)** - Quadratic: Nested loops, bubble sort
- **O(2ⁿ)** - Exponential: Recursive fibonacci, brute force

### Space Complexity
- **In-place algorithms**: O(1) extra space
- **Recursive algorithms**: O(depth) stack space
- **Auxiliary arrays**: O(n) extra space

## 🎓 Practice Problems

1. Implement binary search recursively
2. Sort an array using insertion sort
3. Find kth largest element using heap
4. Implement two-pointer technique
5. Count inversions in array
6. Find median of unsorted array
7. Dutch national flag problem (3-way partition)

## 📚 Additional Resources

- Visualize algorithms at visualgo.net
- Practice at LeetCode, HackerRank
- Study time/space complexity analysis
- Learn algorithm design patterns
- Understand trade-offs between algorithms
