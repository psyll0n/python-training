#!/usr/bin/env python3

# Pattern matching using regex.

import re


""" While there are several steps to using regular expressions in Python, each
step is fairly simple.

1. Import the regex module with import re.
2. Create a Regex object with the re.compile() function. (Remember to use a
raw string.)
3. Pass the string you want to search into the Regex object’s search() method.

This returns a Match object.

Call the Match object’s group() method to return a string of the actual
matched text."""


phoneNumRegex = re.compile(r"(\d{3})-?(\d{3})-(\d{4})")
matchedObject = phoneNumRegex.search("My number is 415-555-1011.")
print("Phone number found: " + matchedObject.group())

# Matched objext groups can be separated with '()' and printed out as shown below.
print(matchedObject.group())
print(matchedObject.group(1))
print(matchedObject.group(2))
print(matchedObject.group(3))
