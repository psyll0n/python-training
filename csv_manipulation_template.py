#! /usr/bin/env python3
# csv_manipulation_template.py - Reads a CSV file and performs manipulation of the data in it.

import csv
from os import error


def read_portfolio(filename, *, errors="warn"):
    """
    Read a CSV file with name, date, shares, price data in a list.
    """
    if errors not in {"warn", "silent", "raise"}:
        raise ValueError("errors must be one of 'warn', 'silent', 'raise'")

    portfolio = []  # List of records.

    with open("Data/portfolio.csv", "r") as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip the header row.
        for rowno, row in enumerate(rows, start=1):
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
            except ValueError as err:
                if errors == "warn":
                    print("Row:", rowno, "Bad row: ", row)
                    print("Row:", rowno, "Reason: ", err)
                elif errors == "raise":
                    raise  # Re-raises the last exception.
                else:
                    pass  # Ignore.
                continue  # Skips to the next row.

            record = {"name": row[0], "date": row[1], "shares": row[2], "price": row[3]}

            portfolio.append(record)
    return portfolio


portfolio = read_portfolio("Data/portfolio.csv")

total = 0.0
for holding in portfolio:
    total += holding["shares"] * holding["price"]  # Shares * price

print("Total cost: ", total)
