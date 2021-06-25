#! python3 
# collections: Counter, namedtuple, OrderedDictionary, defaultdict, dequeue

from collections import defaultdict


d = defaultdict(list)
d['a'] = 1
d['b'] = 2
print(d['c'])