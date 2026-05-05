import pytest
import source.shapes as shapes


# The parametrize decorator is used to run the same test function with different sets of parameters,
# allowing for more comprehensive testing. In this case, we are testing the area of a square with different
# side lengths and expected areas. The `random_param` is included to demonstrate that additional parameters
# can be added without affecting the test logic.
@pytest.mark.parametrize(
    "side_length, expected_area, random_param",
    [
        (2, 4, 12),  # Test case 1: square of 2 should be 4
        (3, 9, 15),  # Test case 2: square of 3 should be 9
        (4, 16, 20),  # Test case 3: square of 4 should be 16
        (5, 25, 25),  # Test case 4: square of 5 should be 25
    ],
)
def test_square_area(side_length, expected_area, random_param):
    assert shapes.Square(side_length).area() == expected_area


# The test function below is similar to the one above, but it tests the perimeter of the square instead of
# the area. The `random_param` is included again to show that it does not affect the test logic, and it can
# be used for additional test scenarios if needed.
@pytest.mark.parametrize(
    "side_length, expected_area, random_param",
    [
        (2, 4, 12),  # Test case 1: square of 2 should be 4
        (3, 9, 15),  # Test case 2: square of 3 should be 9
        (4, 16, 20),  # Test case 3: square of 4 should be 16
        (5, 25, 25),  # Test case 4: square of 5 should be 25
    ],
)
def test_square_perimeter(side_length, expected_area, random_param):
    assert shapes.Square(side_length).perimeter() == 4 * side_length
