# This file defines the Shape class and its subclasses Circle and Rectangle, which include methods
# to calculate area and perimeter.
import math


# Base class for shapes
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


# Circle class that inherits from Shape
class Circle(Shape):
    """
    Circle class that represents a circle shape and provides methods to calculate
    its area and perimeter.

    Attributes:
        radius (float): The radius of the circle.

    Methods:
        area(): Calculates and returns the area of the circle.
        perimeter(): Calculates and returns the perimeter (circumference) of the circle.
    """

    def __init__(self, radius):
        self.radius = radius

    # This method calculates the area of the circle
    def area(self):
        return math.pi * self.radius**2

    # This method calculates the perimeter (circumference) of the circle
    def perimeter(self):
        return 2 * math.pi * self.radius
        expected = 2 * math.pi * self.radius
        assert result == expected, f"Expected {expected}, got {result}"


# Rectangle class that inherits from Shape
class Rectangle(Shape):
    """
    Rectangle class that represents a rectangle shape and provides methods to calculate
    its area and perimeter.

    Attributes:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Methods:
        area(): Calculates and returns the area of the rectangle.
        perimeter(): Calculates and returns the perimeter of the rectangle.
    """

    # The constructor initializes the length and width of the rectangle
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # This method checks if two Rectangle instances are equal based on their length and width
    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.length == other.length and self.width == other.width

    # This method calculates the area of the rectangle
    def area(self):
        return self.length * self.width

    # This method calculates the perimeter of the rectangle
    def perimeter(self):
        return 2 * (self.length + self.width)


# Square class that inherits from Rectangle
class Square(Rectangle):
    """
    Square class that represents a square shape and inherits from the Rectangle class.

    Attributes:
        side (float): The length of the sides of the square.

    Methods:
        area(): Calculates and returns the area of the square.
        perimeter(): Calculates and returns the perimeter of the square.
    """

    # The constructor initializes the side length of the square and calls the parent constructor
    def __init__(self, side):
        super().__init__(length=side, width=side)
