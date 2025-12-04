"""
property_decorator.py - Demonstrates the use of the @property decorator in Python.

The @property decorator allows you to define methods that can be accessed like attributes,
providing a clean interface for encapsulation while enabling validation and computed properties.

Key concepts demonstrated:
- Using @property to create getter methods
- Using @<property>.setter to create setter methods with validation
- Creating read-only computed properties (diameter, area)
- Encapsulation using private attributes (underscore prefix)
"""

class Circle:
    """
    A class representing a circle with radius, diameter, and area properties.
    
    This class demonstrates the use of the @property decorator to:
    1. Provide controlled access to the radius attribute with validation
    2. Calculate derived properties (diameter and area) on-the-fly
    3. Maintain encapsulation by using a private attribute (_radius)
    
    Attributes:
        _radius (float): The private radius attribute of the circle.
    
    Properties:
        radius (float): The radius of the circle (read/write with validation).
        diameter (float): The diameter of the circle (read-only, computed).
        area (float): The area of the circle (read-only, computed).
    """
    
    def __init__(self, radius):
        """
        Initialize a Circle with a given radius.
        
        Args:
            radius (float): The radius of the circle. Must be non-negative.
        
        Note:
            The radius is stored in a private attribute (_radius) to enforce
            encapsulation and enable validation through the property setter.
        """
        self._radius = radius

    @property
    def radius(self) -> float:
        """
        Get the radius of the circle.
        
        Returns:
            float: The current radius value.
        
        Example:
            >>> circle = Circle(5)
            >>> circle.radius
            5
        """
        return self._radius

    @radius.setter
    def radius(self, value: float):
        """
        Set the radius of the circle with validation.
        
        Args:
            value (float): The new radius value.
        
        Raises:
            ValueError: If the radius is negative.
        
        Example:
            >>> circle = Circle(5)
            >>> circle.radius = 10  # Valid
            >>> circle.radius = -5  # Raises ValueError
        """
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value
    
    @property
    def diameter(self) -> float:
        """
        Calculate and return the diameter of the circle.
        
        This is a read-only computed property that is calculated based on
        the current radius value. The diameter is always twice the radius.
        
        Returns:
            float: The diameter of the circle (2 * radius).
        
        Example:
            >>> circle = Circle(5)
            >>> circle.diameter
            10
        
        Note:
            This property is read-only; attempting to set it will raise an error.
        """
        return 2 * self._radius

    @property
    def area(self) -> float:
        """
        Calculate and return the area of the circle.
        
        This is a read-only computed property using the formula: π * r²
        The area is recalculated each time this property is accessed,
        ensuring it's always in sync with the current radius.
        
        Returns:
            float: The area of the circle (π * radius²).
        
        Example:
            >>> circle = Circle(5)
            >>> circle.area
            78.53981633974483
        
        Note:
            This property is read-only; attempting to set it will raise an error.
        """
        import math
        return math.pi * (self._radius ** 2)
    


# ============================================================================
# Example usage demonstrating the @property decorator functionality
# ============================================================================

if __name__ == "__main__":
    # Create a Circle instance with radius 5
    circle = Circle(5)
    
    # Accessing the radius property (uses the getter)
    print("Radius:", circle.radius)  # Output: Radius: 5
    
    # Accessing computed read-only properties
    print("Diameter:", circle.diameter)  # Output: Diameter: 10
    print("Area:", circle.area)      # Output: Area: 78.53981633974483
    
    # Modifying the radius using the setter (includes validation)
    circle.radius = 10
    
    # The computed properties automatically reflect the updated radius
    print("Updated Radius:", circle.radius)  # Output: Updated Radius: 10
    print("Updated Diameter:", circle.diameter)  # Output: Updated Diameter: 20
    print("Updated Area:", circle.area)      # Output: Updated Area: 314.1592653589793
    
    # Attempting to set a negative radius will raise a ValueError
    # Uncomment the following line to see the validation in action:
    # circle.radius = -5  # Raises: ValueError: Radius cannot be negative.