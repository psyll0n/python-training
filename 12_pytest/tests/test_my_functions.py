# This file contains tests for the functions defined in my_functions.py using the pytest framework.
# Each test checks a specific function to ensure it behaves as expected under certain conditions.
import time
import pytest
import source.my_functions as mf


# This test checks the `add` function in my_functions.py
def test_add():
    result = mf.add(number1=13, number2=32)
    assert result == 45


# This test checks the `add` function in my_functions.py for string concatenation
def test_add_strings(number1="Hello, ", number2="world!"):
    result = mf.add(number1=number1, number2=number2)
    assert result == "Hello, world!"


# This test checks the `subtract` function in my_functions.py
def test_subtract():
    result = mf.subtract(number1=13, number2=32)
    assert result == -19


# This test checks the `multiply` function in my_functions.py
def test_multiply():
    result = mf.multiply(number1=13, number2=32)
    assert result == 416


# This test checks the `divide` function in my_functions.py
def test_divide():
    result = mf.divide(number1=42, number2=7)
    assert result == 6


# This test checks the `divide` function in my_functions.py for division by zero
def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        mf.divide(number1=42, number2=0)


# The section below demonstrates the use of pytest markers to categorize tests and control their execution.


# The `mark.slow` decorator is used to mark this test as a slow test, which can be useful for
# categorizing tests and running them selectively.
@pytest.mark.slow
def very_slow_test():
    time.sleep(5)
    result = mf.divide(number1=13503, number2=57)
    assert result == 237


# The `mark.skip` decorator is used to skip this test, and the reason for skipping is provided as an
# argument.
@pytest.mark.skip(
    reason="This test is skipped because it is currently broken and needs to be fixed."
)
def test_skip():
    result = mf.add(number1=10, number2=20)
    assert result == 30


# The `mark.xfail` decorator is used to mark this test as an expected failure, and the reason for the expected failure
# is provided as an argument.
@pytest.mark.xfail(
    reason="This test is expected to fail because the function is not implemented correctly yet."
)
def test_expected_failure():
    result = mf.subtract(number1=10, number2=5)
    assert result == 6  # This assertion is intentionally incorrect to demonstrate xfail
