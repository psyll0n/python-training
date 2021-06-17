import os
import subprocess
import shutil
from pprint import pprint


# Get your current working directly.
# This returns a string.
print("-" * 50)
my_cwd = os.getcwd()
print(my_cwd)
print("-" * 50)


# List the contents of a directory.
# This returns a list.
dir_list = os.listdir()
for item in dir_list:
    print(item)


print("-" * 50)
print("This is the contents of the current directory...")
# Get the Absolute Path name of a file (file + current working dir)
print(os.path.abspath("."))
print("-" * 50)
