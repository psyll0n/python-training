#! python3
# sequence_reader.py - Auxiliary python script used to read the sequence of numbers generated with recaman_sequence.py.

from os import name
import sys


def read_series(filename):
    with open(filename, mode="rt", encoding="utf-8") as f:
        return [int(line.strip()) for line in f]


def main(filename):
    series = read_series(filename)
    print(series)


if __name__ == "__main__":
    main("recaman.dat")
