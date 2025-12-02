#!/usr/bin/env python3
"""basic_function.py - Demonstrates basic function definition and calling.

This module shows:
- How to define functions with parameters
- How to call functions with arguments
- The standard Python main() pattern
- The __name__ == "__main__" idiom for script execution
"""


def main():
    """Main entry point for the program.
    
    Calls the kitten function with three arguments.
    """
    kitten(5, 6, 7)


def kitten(a, b, c):
    """Print three values and a meow message.
    
    Args:
        a: First value to print
        b: Second value to print
        c: Third value to print
    """
    print(a, b, c)
    print("Meow")


# Execute main() only when script is run directly (not imported)
if __name__ == "__main__":
    main()
