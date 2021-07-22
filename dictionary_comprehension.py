#!/usr/bin/env python3
# dictionary_comprehension.py

# Create a dictionary containing the months of the year.
months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}

print(months)


# Create a new dictionary that reverses the keys and values of the months dictionary.
months2 = {number: name for name, number in months.items()}

print(months2)


# Create a dictionary containing the grades of 3 students.
grades = {"Sue": [100, 85, 95], "John": [100, 85, 95], "Jane": [100, 85, 95]}

# Calcuate the average grade for each student.
grades2 = {k: sum(v) / len(v) for k, v in grades.items()}


print(grades2)
