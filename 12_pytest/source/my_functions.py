# This file contains basic mathematical functions that can be used in various applications.
def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    if number2 == 0:
        raise ValueError("Cannot divide by zero.")
    return number1 / number2
