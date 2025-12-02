#!/usr/bin/env python3
"""class_definition.py - Demonstrates fundamental class definition in Python.

This module covers:
- Class vs instance attributes
- Constructor (__init__) method
- Instance methods
- Creating and using objects

Key Concepts:
- Class attributes are shared by all instances
- Instance attributes are unique to each object
- self refers to the current instance
"""


class Car:
    """Represents a car with make, model, year, color, and optional moon roof.
    
    Class Attributes:
        tires (int): Number of tires (shared by all cars)
    
    Instance Attributes:
        make (str): Car manufacturer
        model (str): Car model name
        year (str): Year of manufacture
        color (str): Car color
        moon_roof (bool): Whether car has a moon roof
        engine_running (bool): Current engine state
    """
    
    # Class Attributes / Variables - shared by ALL instances of Car
    tires = 4

    # Class Constructor / Initializer (Special method called when creating objects)
    def __init__(self, make, model, year, color, moon_roof=False):
        """Initialize a new Car instance.
        
        Args:
            make (str): Car manufacturer (e.g., "Ford", "Tesla")
            model (str): Model name (e.g., "Mustang", "Model 3")
            year (str): Year of manufacture
            color (str): Car color
            moon_roof (bool, optional): Has moon roof. Defaults to False.
        """
        # Instance Attributes / Variables - unique to each Car object
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.moon_roof = moon_roof
        self.engine_running = False  # All cars start with engine off

    # Instance Methods - functions that operate on the object
    def start_the_engine(self):
        """Start the car's engine."""
        self.engine_running = True

    def stop_the_engine(self):
        """Stop the car's engine."""
        self.engine_running = False


def main():
    """Main function demonstrating Car class usage."""
    print("Hello from the main() method!")
    
    # Create two Car instances with different attributes
    car1 = Car("Ford", "Mustang", "2010", "Blue")
    car2 = Car("Tesla", "Model 3", "2020", "Red", True)  # Has moon roof

    # Accessing car1 instance attributes
    print("Printing car1 details:".center(50, "-"))
    print("Make:  {}".format(car1.make))
    print("Model: {}".format(car1.model))
    print("Year:  {}".format(car1.year))
    print("Color: {}".format(car1.color))
    print("Moon Roof: {}".format(car1.moon_roof))

    # Accessing car2 instance attributes
    print("Printing car2 details:".center(50, "-"))
    print("Make:  {}".format(car2.make))
    print("Model: {}".format(car2.model))
    print("Year:  {}".format(car2.year))
    print("Color: {}".format(car2.color))
    print("Moon Roof: {}".format(car2.moon_roof))

    # Accessing class attributes (same for all instances)
    print("Class Attributes:".center(50, "-"))
    print("car1: ", car1.tires)  # Accessed through instance
    print("car2: ", car2.tires)  # Accessed through instance
    print("Car: ", Car.tires)    # Accessed through class


if __name__ == "__main__":
    main()
