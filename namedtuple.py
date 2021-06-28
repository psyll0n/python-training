#! python3
# collections: Counter, namedtuple, OrderedDictionary, defaultdict, dequeue

from collections import namedtuple

Point = namedtuple("Point", "x,y")
pt = Point(1, -4)
print(pt)
