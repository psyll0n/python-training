#! python3

import calculator_ascii_art, os

# A flag to keep the calculator running
should_continue = True

# Print ASCII art logo and welcome message
print(calculator_ascii_art.logo)
print("Welcome to the Simple Calculator App!")


# Define four functions for basic arithmetic operations

def add(n1, n2):
    """
    Adds two numbers and returns the result.
    
    Args:
        n1 (float): First number.
        n2 (float): Second number.
        
    Returns:
        float: Sum of n1 and n2.
    """
    return n1 + n2


def subtract(n1, n2):
    """
    Subtracts the second number from the first and returns the result.
    
    Args:
        n1 (float): First number.
        n2 (float): Second number.
        
    Returns:
        float: Difference of n1 and n2.
    """
    return n1 - n2


def multiply(n1, n2):
    """
    Multiplies two numbers and returns the result.
    
    Args:
        n1 (float): First number.
        n2 (float): Second number.
        
    Returns:
        float: Product of n1 and n2.
    """
    return n1 * n2


def divide(n1, n2):
    """
    Divides the first number by the second and returns the result.
    
    Args:
        n1 (float): First number.
        n2 (float): Second number.
        
    Returns:
        float: Quotient of n1 and n2.
        
    Raises:
        ZeroDivisionError: If n2 is zero.
    """
    if n2 == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return n1 / n2


# Dictionary to map operation symbols to corresponding functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def clear_screen():
    """
    Clears the terminal screen using the appropriate command for the user's operating system.
    """
    # Check if the system is Windows, then use 'cls'. Otherwise, use 'clear'.
    if os.name == 'nt':  # 'nt' stands for Windows
        os.system('cls')
    else:
        os.system('clear')


# Main calculator function
def calculator():
    """
    Runs the main logic for the calculator, allowing the user to input two numbers
    and perform a specified mathematical operation (+, -, *, /). The user can continue 
    operating with the result of the previous calculation or start a new one.
    """
    
    should_accumulate = True
    
    # Get the first number from the user
    num1 = float(input("Specify the first number: \n"))

    while should_accumulate:
        # Get the operation symbol from the user
        operation_symbol = input("Specify a mathematical operation '+', '-', '*', '/': \n")
        
        # Get the second number from the user
        num2 = float(input("Specify the second number: \n"))
    
        # Check if the operation is valid
        if operation_symbol in operations:
            # Perform the operation and store the result
            result = operations[operation_symbol](num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {result}")
        else:
            # Invalid operation message
            print("You did not specify a valid mathematical operation...")

        # Ask the user if they want to continue with the result
        choice = input("Would you like to continue working with the previous result? Type 'yes' or 'no' ... ").lower()

        if choice == "no":
            # Exit the loop if the user chooses 'no'
            should_accumulate = False
            print("Goodbye!")
        else:
            # Update num1 with the result and continue
            num1 = result
            # Call the Clear screen function
            clear_screen()
            print(f"Continuing with {num1} ...")

# Start the calculator
calculator()
