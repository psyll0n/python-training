#! python3
# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

from itertools import groupby


def smaller_than_6(x):
    return x < 6

a = [9, 8, 7, 6, 5, 4, 3, 2, 1]
group_obj = groupby(a, key=smaller_than_6)
for key, value in group_obj:
    print(key, list(value))
    
    

persons = [{'name': 'Tim', 'age': 25}, {'name': 'John', 'age': 25}, {'name': 'Nina', 'age': 31},
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}, {'name': 'Bob', 'age': 29},]

group_obj2 = groupby(persons, key=lambda x: x['age'])
for key in group_obj2:
    print(key, list(value))