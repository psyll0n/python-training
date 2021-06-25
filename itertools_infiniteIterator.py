#! python3
# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

from itertools import count, cycle, repeat

for i in count(10):
    print(i)
    if i == 10000:
        break
    

a = [1, 2, 3, 4, 5]
for i in cycle(a):
    print(i)
    if i == 5:
        break


b = [1, 2, 3, 4, 5]
for i in repeat(1, 4):
    print(i)
