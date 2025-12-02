#!/usr/bin/env python3

# Import modules for random number generation.
import random

# Import Counter class for counting.
from collections import Counter

# Generate random values and store those in a list.
numbers = [random.randrange(1, 6) for i in range(50)]

# Create a Counter object to count the number of occurrences
counter = Counter(numbers)

for value, count in sorted(counter.items()):
    print(f"{value:<4}{count}")
