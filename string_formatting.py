# To make sure a string will display as expected, we can format the result with the format() method.

# The format() method allows you to format selected parts of a string.

# Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?

# To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method:

price = input("Specify the price per unit: ")
txt = "The price is {} dollars."
print(txt.format(price))


items = input("Specify the number of items: ")
txt = "The number of items is {}: "
print(txt.format(items))

# If you want to use more values, just add more values to the format() method.
# You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))


#  You can also use named indexes by entering a name inside the curly brackets {carname},
# but then you must use names when you pass the parameter values txt.format(carname = "Ford"):

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
