# This one is like the scripts with argv.

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#  The first function can be alternatively defined as follows.

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# The next function takes one argument.

def print_one(arg1):
    print(f"arg1: {arg1}")

# The function below takes no arguments.

def print_none():
    print("I got nothing...")

print_two("Alex","Yakimov")
print_two_again("Alex","Yakimov")
print_one("First!")
print_none()
