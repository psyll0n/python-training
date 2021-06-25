#! python3
# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

from itertools import permutations


a = [1, 2, 3]
perm = permutations(a)
print(list(perm))
