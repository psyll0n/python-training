# The `conftest.py` file is used to define global fixtures that can be shared across multiple test files.
import pytest
import source.shapes as shapes


# The Pyton fixture is used to create a reusable instance of the Rectangle class for testing purposes.
@pytest.fixture
def rectangle():
    return shapes.Rectangle(length=5, width=3)


# Another fixture to create a different instance of the Rectangle class for testing purposes.
@pytest.fixture
def another_rectangle():
    return shapes.Rectangle(length=10, width=2)
