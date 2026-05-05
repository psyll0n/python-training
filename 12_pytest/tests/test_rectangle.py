# This file contains unit tests for the Rectangle class defined in shapes.py, using pytest framework.
import math
import pytest
import source.shapes as shapes


# The setup_method and teardown_method functions are used to print messages before and after each test method is executed, respectively.
# This method will be called before each test method is executed
def setup_method(method):
    print(f"Setting up for {method}")


# This method will be called after each test method is executed
def teardown_method(method):
    print(f"Tearing down after {method}")


# Test to check if the length and width are set correctly
def test_dimensions(rectangle):
    assert rectangle.length == 5
    assert rectangle.width == 3


# Test to check if the area is calculated correctly
def test_area(rectangle):
    assert rectangle.area() == rectangle.length * rectangle.width


# Test to check if the perimeter is calculated correctly
def test_perimeter(rectangle):
    assert rectangle.perimeter() == 2 * (rectangle.length + rectangle.width)


# Test to check if two rectangles with different dimensions are not equal
def test_not_equal(rectangle, another_rectangle):
    assert rectangle.length != another_rectangle.length
    assert rectangle.width != another_rectangle.width


# Test to check if the area of two rectangles with different dimensions are not equal
def test_area_not_equal(rectangle, another_rectangle):
    assert rectangle.area() != another_rectangle.area()
