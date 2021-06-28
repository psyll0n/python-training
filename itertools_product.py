#! python3
# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

from itertools import product


a = [1, 2, 3, 4, 5]
b = [9, 8, 7, 6, 5]

prod = product(a, b)
print(list(prod))
