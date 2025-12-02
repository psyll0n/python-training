# Data Structures

Python data structures and comprehension techniques. This section covers the fundamental data structures and efficient ways to create and manipulate them.

## 📂 Contents

### [Data Structures](./data_structures/)
Core Python data structures with practical examples.

#### Lists
- **lists_example.py** - List operations: split(), pop(), append(), join(), slicing
- **list_comprehension.py** - Creating lists with comprehension syntax
- **linked_list_example.py** - Custom linked list implementation with Node class
- **nested_list.py** - Working with multi-dimensional lists
- **directory_listing.py** - Using os.listdir() with lists
- **directory_listing2.py** - Advanced directory listing
- **create_name_age_list.py** - Combining related data in lists
- **issorted_list.py** - Checking if a list is sorted

#### Dictionaries
- **dictionary_example2.py** - Basic dictionary operations and key-value pairs
- **dictionary_methods.py** - Common dictionary methods (keys(), values(), items())
- **dictionary_iteration.py** - Iterating through dictionaries
- **looping_thru_dictionaries.py** - Various looping patterns
- **nested_dictionaries_example.py** - Multi-level dictionary structures
- **grade_book.py** - Practical example: student grades
- **hashtable_example.py** - Hash table implementation
- **orderedDict.py** - Maintaining insertion order with OrderedDict

**Projects:**
- **secret_auction/** - Blind auction program using dictionaries

#### Sets
- Set operations and methods
- Set comprehensions
- Mathematical set operations (union, intersection, difference)

#### Tuples
- Immutable sequences
- Tuple unpacking
- Use cases for tuples vs lists

#### Mixed Data Structures
- **mixed_data_structures.py** - Combining lists, dicts, sets, tuples
- **mixed_data_structures2.py** - Complex nested structures

**Key Concepts:** Lists, dictionaries, sets, tuples, indexing, slicing, methods

---

### [List Comprehension](./list_comprehension/)
Efficient and Pythonic list creation.

- **main.py** - Comprehensive guide with 7 different patterns:
  1. Simple transformation (add 1 to each number)
  2. Mathematical operations (squaring numbers)
  3. Using range() in comprehensions
  4. Filtering with conditions (short names)
  5. Transformation + filtering (uppercase long names)
  6. Type conversion + filtering (even numbers from strings)
  7. File processing (finding common numbers)

**Syntax:**
```python
[expression for item in iterable if condition]
```

**Key Concepts:** Comprehension syntax, filtering, transformation, lazy evaluation

---

### [Dictionary Comprehension](./dictionary_comprehension/)
Create and transform dictionaries efficiently.

- Dictionary comprehension syntax and patterns
- Creating dictionaries from iterables
- Filtering and transforming key-value pairs
- Converting between data structures

**Syntax:**
```python
{key_expr: value_expr for item in iterable if condition}
```

**Key Concepts:** Dict comprehensions, key-value transformations, filtering

---

## 📊 Data Structure Comparison

| Structure | Ordered | Mutable | Duplicates | Use Case |
|-----------|---------|---------|------------|----------|
| **List** | ✓ | ✓ | ✓ | Ordered collection of items |
| **Tuple** | ✓ | ✗ | ✓ | Immutable ordered data |
| **Set** | ✗ | ✓ | ✗ | Unique items, fast membership testing |
| **Dict** | ✓ (3.7+) | ✓ | Keys: ✗, Values: ✓ | Key-value mappings |

## 🎯 Learning Path

1. **Lists** - Start with the most versatile structure
2. **Dictionaries** - Learn key-value mappings
3. **List Comprehension** - Write more Pythonic code
4. **Dictionary Comprehension** - Efficient dict creation
5. **Sets and Tuples** - Understand when to use each
6. **Mixed Structures** - Combine structures for complex data

## 💡 Tips

- Use comprehensions for simple transformations (more readable)
- Lists are great for ordered collections
- Dictionaries excel at lookups by key
- Sets are perfect for removing duplicates
- Tuples protect data from modification
- Choose the right structure for your use case

## ⚡ Performance Notes

- List access by index: O(1)
- Dictionary access by key: O(1) average
- Set membership test: O(1) average
- List search: O(n)
- Comprehensions are generally faster than loops
