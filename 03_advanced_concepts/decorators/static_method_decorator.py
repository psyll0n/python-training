# static_method_decorator.py - Demonstrates the use of the `@staticmethod` decorator in Python.

class Math:
    """
    A class that provides static methods for basic mathematical operations.

    Static methods do not depend on class or instance state and can be called directly on the class.
    """

    @staticmethod
    def add(x: int, y: int) -> int:
        """
        Return the sum of x and y.

        Args:
            x (int): The first number.
            y (int): The second number.

        Returns:
            int: The sum of x and y.
        """
        return x + y

    @staticmethod
    def subtract(x: int, y: int) -> int:
        """
        Return the difference of x and y.

        Args:
            x (int): The number to subtract from.
            y (int): The number to subtract.

        Returns:
            int: The difference of x and y.
        """
        return x - y

    @staticmethod
    def multiply(x: int, y: int) -> int:
        """
        Return the product of x and y.

        Args:
            x (int): The first number.
            y (int): The second number.

        Returns:
            int: The product of x and y.
        """
        return x * y

    @staticmethod
    def divide(x: int, y: int) -> float:
        """
        Return the quotient of x and y.

        Args:
            x (int): The numerator.
            y (int): The denominator. Must not be zero.

        Returns:
            float: The result of division x / y.

        Raises:
            ValueError: If y is zero.
        """
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        return x / y


# Example usage of the Math class and its static methods:
if __name__ == "__main__":
    print("Addition:", Math.add(5, 3))          # Output: 8
    print("Subtraction:", Math.subtract(5, 3))  # Output: 2
    print("Multiplication:", Math.multiply(5, 3))  # Output: 15
    print("Division:", Math.divide(5, 2))        # Output: 2.5
    try:
        print("Division by zero:", Math.divide(5, 0))
    except ValueError as e:
        print(e)  # Output: Cannot divide by zero.