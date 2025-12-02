#! /usr/bin/env python3
# csv_manipulation_template.py - Reads a CSV file and performs manipulation of the data in it.
# Use with csv_filereader.py

from . import csv_reader  # Package-relative import
from os import error


def read_portfolio(filename, *, errors="warn"):
    """
    Read a CSV file with name, date, shares, price data in a list.
    """
    return csv_reader.read_csv(filename, [str, str, int, float], errors=errors)


if __name__ == "__main__":
    portfolio = read_portfolio("Data/portfolio.csv")

    total = 0.0
    for holding in portfolio:
        total += holding["shares"] * holding["price"]  # Shares * price

    print("Total cost: ", total)
