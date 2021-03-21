# Import the 're' pythone regex module.

import re as regex_module

txt = "The rain in Spain"
x = regex_module.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")


# The findall() function returns a list containing all matches.

txt = "The rain in Spain"
x = regex_module.findall("ai", txt)
print(x)

txt = "The rain in Spain"
x = regex_module.findall("Portugal", txt)
print(x)


# The search() function searches the string for a match, and returns a Match object if there is a match.

txt = "The rain in Spain"
x = regex_module.search("\s", txt)

print("The first white-space character is located in position:", x.start())


# The split() function returns a list where the string has been split at each match:

txt = "The rain in Spain"
x = regex_module.split("\s", txt)
print(x)


# You can control the number of occurrences by specifying the maxsplit parameter:

txt = "The rzin in Spain"
x = regex_module.split("\s", txt, 1)
print(x)


# The sub() function replaces the matches with the text of your choice:

txt = "The rain in Spain"
x = regex_module.sub("\s", "9", txt)
print(x)

# Replace the first 2 occurrences:

txt = "The rain in Spain"
x = regex_module.sub("\s", "9", txt, 2)
print(x)
