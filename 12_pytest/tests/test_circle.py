import pytest
import math
import source.shapes as shapes


class TestCircle:

    # This method will be called before each test method is executed
    def setup_method(self, method):
        print(f"Setting up for {method}")
        self.circle = shapes.Circle(radius=10)

    # This method will be called after each test method is executed
    def teardown_method(self, method):
        print(f"Tearing down after {method}")
        del self.circle

    # Test to check if the radius is set correctly
    def test_radius(self):
        assert self.circle.radius == 10

    # Test to check if the area is calculated correctly
    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius**2

    # Test to check if the perimeter is calculated correctly
    def test_perimeter(self):
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius
