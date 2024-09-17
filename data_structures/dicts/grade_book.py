#!/usr/bin/env python3
# grade_book.py

"""Using a dictionary to represent an instructor's grade book."""

grade_book = {
    "Susan": [92, 85, 100],
    "Eduardo": [83, 95, 88],
    "David": [75, 65, 78],
    "Pantipa": [95, 95, 95],
}


all_grades_total = 0
all_grades_count = 0


# Unpack the keys and values in the dictionary. Loop through the dictionary values and calculate the class average.
for name, grades in grade_book.items():
    total = sum(grades)
    all_grades_total += sum(grades)
    all_grades_count += len(grades)

print(f"Class's average: {all_grades_total / all_grades_count:.2f}")
