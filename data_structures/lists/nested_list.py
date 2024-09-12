# Nested lists Example
fruits = ["Strawberies", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pear"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

# Print the first list nested list in the `dirty_dozen` list of lists
print(dirty_dozen[0])

# Print the second list nested list in the `dirty_dozen` list of lists
print(dirty_dozen[1])

# Print the second item in the second nested list - `vegetables`
print(dirty_dozen[1][2])
# Print the third item in the second nested list - `vegetables`
print(dirty_dozen[1][3])