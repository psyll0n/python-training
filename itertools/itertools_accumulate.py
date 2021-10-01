#! python3
# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

from itertools import accumulate
import operator

a = [1, 2, 3, 4, 5]
acc = accumulate(a, func=operator.mul)
print(a)
print(list(a))
