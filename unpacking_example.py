# Example unplacking of arguments.

from sys import argv, version
import warnings

warnings.filterwarnings("ignore")

try:
    script, first, second, third = argv
    print("The script is called:", script)
    print("Your first variable is:", first)
    print("Your third variable is:", second)
    print("Your fourth variable is:", third)
except:
    print("example: python3 unpacking_example.py <first_arg> <second_arg> <third_arg>")
