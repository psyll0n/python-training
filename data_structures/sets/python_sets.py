#!/usr/bin/env python3
# python3_sets.py

colors = {
    "red",
    "green",
    "blue",
    "yellow",
    "orange",
    "white",
    "black",
    "cyan",
    "red",
    "blue",
}

print(len(colors))

for color in colors:
    print(color.upper(), end=" ")

# Removing Duplicates through the use of a set()
set(colors)

print(colors)

numbers = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
]

ordered_set = set(numbers)

print(ordered_set)
