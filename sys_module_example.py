#!/usr/bin/env python3

import sys

print("This script checks what version of Python is running on your system.")


# Check python version with the 'sys' module.
if sys.version_info.major < 3:
    print("You need to update your Python version.")
elif sys.version_info.minor < 7:
    print("You are not running the latest version of Pytho.")
else:
    print("All is good!")
