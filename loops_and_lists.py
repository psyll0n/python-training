the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']


# This first for-loop goes through a list.
for number in the_count:
    print(f'This is count {number}')

# Another for-loop similar to the one above.
for fruit in fruits:
    print(f'A fruit of type: {fruit}')

# It is also possible to go through a mixed list. Use {} for
# this purpose.
for i in change:
    print(f'I got {i}')

# Another option is to build a list by creating an empty one first.
elements = []

# The range function is used to do 0 to 5 counts
for i in range(0, 5):
    print(f'Adding {i} to the list.')
    # Apped is a function that lists understand.
    elements.append(i)

# Now let's print the new list too.
for i in elements:
    print(f'Element was: {i}')
