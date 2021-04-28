# Define a list of lists called items.
items = [[0, 'a', 2],[5, 'b', 0],[2, 'c', 1]]
print(items)

print("The first output is produced by a function called 'second'.")
def second(item):
    '''Sorts and returns the second entry in items list of lists.'''
    return[1]

print(sorted(items, key=second))

print("The second output is produced by a lambda function.")
'''Lambda function example doing the same operation.'''
sorted(items, key=lambda item: item[1])
