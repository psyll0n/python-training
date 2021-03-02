

# Create a list called 'fruits'.
fruits = ['apple', 'banana', 'apricot', 'cherry', 'pineapple', 'mango']

# Define a second empty list called 'newlist'.

newlist = []

# Loop through the items in the 'fruits' list and append those containing the letter 'a' to 'newlist'.

for x in fruits:
    if "a" in x:
    	newlist.append(x)


print(fruits)
print(newlist)


# Shorthand syntax
# newlist = [expression for item in iterable if condition == True]


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlistoffruits = [x for x in fruits if "a" in x]

print(newlistoffruits)


fruitlist = [x for x in fruits if x != "apple"]
print(fruitlist)


# Use of 'range()'

listofnumbers = [x for x in range(10) if x < 5]
print(listofnumbers)


