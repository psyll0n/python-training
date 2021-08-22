#!/usr/bin/env python3

from math import pi


def main():
    seq = range(11)
    seq2 = [round(pi, i) for i in seq]
    print(seq2)
    print_list(seq)
    print_list(seq2)


def print_list(o):
    for x in o:
        print(x, end=" ")
    print()


if __name__ == "__main__":
    main()
