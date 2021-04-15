# The 'try' block lets you test a block of code for errors.

# The 'except' block lets you handle the error.

# The 'finally' block lets you execute code, regardless of the result of the try- and except blocks.

# x = input("Enter a number: ")

# print("You entered " + x)


try:
    print(x)
except NameError:
    print("Variable x is not defined.")
except:
    print("Something else went wrong.")

try:
    print("Hello")
except:
    print("Something went wrong.")
else:
    print("Nothing went wrong.")

try:
    print(x)
except:
    print("Something went wrong.")
finally:
    print("The 'try except' is finished.")

# Try to open and write to a file that is not writable:

try:
    f = open("demofile.txt")
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file.")
finally:
    f.close()

# As a Python developer you can choose to throw an exception if a condition occurs.
# To throw (or raise) an exception, use the 'raise' keyword.

x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero.")


# The raise keyword is used to raise an exception.
# You can define what kind of error to raise, and the text to print to the user.

x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed.")
