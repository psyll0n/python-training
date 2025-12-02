#! python3
# string_to_int_converter.py - A script that converts strings into integers.

import sys

DIGIT_MAP = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def convert(s):
    """Convert a string to an integer."""
    try:
        number = ""
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        return True, x
    except (KeyError, TypeError) as e:
        return False, repr(e)


if __name__ == "__main__":
    # Prompt user for input
    user_input = input("Enter a number using words (e.g., 'two three four'): ")

    # Split the user input into words
    input_list = user_input.lower().split()

    # Call the convert function with user input
    success, result = convert(input_list)

    if success:
        print(f"Conversion succeeded! x = {result}")
    else:
        print(f"Conversion error: {result}", file=sys.stderr)
