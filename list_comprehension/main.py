numbers = [1, 2, 3]

new_list = [n + 1 for n in numbers]

print(new_list)


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [n**2 for n in numbers]

print(squared_numbers)


range(1, 5)

new_items_list = [num * 2 for num in range(1, 5)]

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

short_names = [name for name in names if len(name) < 5]

print(short_names)


capitalized_names = [name.upper() for name in names if len(name) > 5]

print(capitalized_names)


list_of_strings = ["9", "0", "32", "8", "2", "8", "64", "29", "42", "99"]

numbers = [int(i) for i in list_of_strings]

result = [i for i in numbers if i % 2 == 0]

print(result)

# The example below creates a list called result which contains the numbers that are  common in two
# separate files.

# Read the contents of file1.txt and file2.txt

with open("file1.txt") as file1:
    file1_numbers = file1.readlines()

with open("file2.txt") as file2:
    file2_numbers = file2.readlines()

# Convert the read lines into a list of integers

file1_numbers = [int(num.strip()) for num in file1_numbers]

file2_numbers = [int(num.strip()) for num in file2_numbers]

# Use list comprehension to find common numbers

result = [num for num in file1_numbers if num in file2_numbers]

# Print the result

print(result)
