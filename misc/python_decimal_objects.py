#!/usr/bin/env python3
# python_decimal_objects.py - Decimal Objects are used for precision calculations.


from decimal import Decimal


amount = 112.31

print(f"{amount:.20f}")


principal = Decimal("1000.00")
print(type(principal))

rate = Decimal("0.05")
print(type(rate))

x = Decimal("10.5")
y = Decimal("2")

print(x // y)
print(x + y)


for year in range(1, 11):
    amount = principal * (1 + rate) ** year
    print(f"{year:>2}{amount:>10.2f}")
