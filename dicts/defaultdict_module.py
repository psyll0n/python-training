#! python3
# collections: Counter, namedtuple, OrderedDictionary, defaultdict, dequeue
# Examples demonstrating how the defaultdict module can be used in different contexts:

from collections import defaultdict


d = defaultdict(list)
d["a"] = 1
d["b"] = 2
print(d["a"],d["b"])

# Grouping Items by Key
# In this example, we use a defaultdict(list) to group words by their starting letter.
words = ["apple", "banana", "apricot", "blueberry", "avocado", "blackberry"]
grouped_words = defaultdict(list)

for word in words:
    grouped_words[word[0]].append(word)

print(grouped_words)
# Output: defaultdict(<class 'list'>, {'a': ['apple', 'apricot', 'avocado'], 'b': ['banana', 'blueberry', 'blackberry']})

# Counting Occurrences with int Default
# A defaultdict(int) is useful for counting occurrences. 
# This behaves like a normal dictionary but initializes missing keys with 0.
chars = "aabbccaaa"
char_count = defaultdict(int)

for char in chars:
    char_count[char] += 1

print(char_count)
# Output: defaultdict(<class 'int'>, {'a': 5, 'b': 2, 'c': 2})

# Accumulating Values in a Set
# Using defaultdict(set) to collect unique values associated with keys.
data = [("apple", "fruit"), ("carrot", "vegetable"), ("apple", "snack"), ("carrot", "healthy")]
category_map = defaultdict(set)

for item, category in data:
    category_map[item].add(category)

print(category_map)
# Output: defaultdict(<class 'set'>, {'apple': {'fruit', 'snack'}, 'carrot': {'vegetable', 'healthy'}})

# Nested defaultdicts
# You can create a nested structure using defaultdict to avoid manually checking if a key exists.
nested_dict = defaultdict(lambda: defaultdict(int))
nested_dict["outer"]["inner"] += 1

print(nested_dict)
# Output: defaultdict(<function <lambda> at 0x...>, {'outer': defaultdict(<class 'int'>, {'inner': 1})})

# Using defaultdict to Build an Adjacency List
# When working with graphs, defaultdict(list) can represent an adjacency list, making it easier to handle edges dynamically.
edges = [("A", "B"), ("A", "C"), ("B", "C"), ("C", "A")]
graph = defaultdict(list)

for u, v in edges:
    graph[u].append(v)

print(graph)
# Output: defaultdict(<class 'list'>, {'A': ['B', 'C'], 'B': ['C'], 'C': ['A']})


# Handling Missing Keys with lambda
# Using lambda to set a default value for a dictionary when a key doesn't exist.
# Default factory returns "Not Present" if key is missing
d = defaultdict(lambda: "Not Present")
d["key1"] = "value1"

print(d["key1"])  # Output: value1
print(d["key2"])  # Output: Not Present
