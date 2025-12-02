#!/usr/bin/env python3
# csv_filereader.py - Reads CSV files and performs conversion into a list of dictionaries.

import csv


def read_csv(filename, types, *, errors="warn"):
    """
    Read a CSV file with type conversion into a list of dictionaries.
    """
    if errors not in {"warn", "silent", "raise"}:
        raise ValueError("errors must be one of 'warn', 'silent', 'raise'")

    records = []  # List of records
    with open(filename, "r") as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip the header row.

        for rowno, row in enumerate(rows, start=1):
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as err:
                if errors == "warn":
                    print("Row: ", rowno, "Bad row: ", row)
                    print("Row: ", rowno, "Reason: ", err)
                elif errors == "raise":
                    raise  # Re-raises the last exception.
                else:
                    pass
                continue
            record = dict(zip(headers, row))
            records.append(record)
    return records
