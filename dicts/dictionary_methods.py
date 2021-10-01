#!/usr/bin/env python3
# Dictionary methods

months = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}

# Displays the keys in the dictionary.
for month_name in months.keys():
    print(month_name, end=" ")

# Displays the values in the dictionary.
for month_name in months.values():
    print(month_name, end=" ")

# Displays the items in the dictionary.
months_view = months.keys()

# Displays the key-value pairs in the dictionary.
for key in months_view:
    print(key, end=" ")

# Displays the key-value pairs in the dictionary.
print(list(months.keys()))
print(list(months.items()))

# Displays the key-value pairs in the dictionary.
for month_name in sorted(months.keys()):
    print(month_name, end=" ")


country_capitals1 = {"France": "Paris", "Spain": "Madrid", "Italy": "Rome"}

country_capitals2 = {"Nepal": "Kathmandu", "India": "New Delhi", "Bhutan": "Thimphu"}

country_capitals3 = {"Spain": "Madrid", "Italy": "Rome", "France": "Paris"}


# Comparison between dictionaries.
country_capitals1 == country_capitals2

country_capitals1 == country_capitals3

country_capitals1 != country_capitals2


# Demonstrate the dictionary update method.
country_codes = {}

country_codes.update({"UK": "United Kingdom"})

print(country_codes)

country_codes.update(Austria="AU")

print(country_codes)
