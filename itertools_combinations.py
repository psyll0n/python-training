#! python3
# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

from itertools import combinations, combinations_with_replacement

a = [1, 2, 3, 4, 5, 6, 7]
comb = combinations(a, 2)
print(list(comb))


comb_wr = combinations_with_replacement(a, 3)
print(list(comb_wr))