#! python3
# collections: Counter, namedtuple, OrderedDictionary, defaultdict, dequeue

from collections import Counter

a = "aaaabbbbbbbbccccccc"
my_counter = Counter(a)
print(my_counter.values())
print(my_counter.most_common(1)[0][0])

print(list(my_counter.elements()))

