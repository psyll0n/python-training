"""Simple Calculator - Division with High Precision.

A basic calculator that divides two numbers and displays the result
with 50 decimal places of precision using Python's float formatting.

Features:
- User input for two numbers
- Division operation
- High-precision output (50 decimal places)
"""

x = int(input("x: "))
y = int(input("y: "))

z = x / y
print(f"{z:.50f}")  # Display result with 50 decimal places
