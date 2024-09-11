# Import the already created python_module_example-a.py module in this script.
# Also import the built-in python module 'platform'.
# The third line shows how to import only a specific value from a dictionary.
# The 'datetime' module displays the current date


import datetime
import python_module_example_a as module_a
import platform as module_b
from python_module_example_a import person1


x = datetime.datetime.now()
print(x)

# Return the year and name of weekday:

print(x.year)
print(x.strftime("%A"))

# To create a date, we can use the datetime() class (constructor) of the datetime module.
# The datetime() class requires three parameters to create a date: year, month, day.

x = datetime.datetime(2020, 5, 17)
print(x)

module_a.greeting("Alexander")

a = module_a.person1["age"]
print(a)


x = module_b.system()
print("This systems is running: " + x)


x = dir(module_b)
print(x)


print(person1["age"])


y = dir(module_a)
print(y)
