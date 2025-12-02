#!/usr/bin/env python3


def generator(start, stop):
    while start <= stop:
        yield start
        print(f"start = {start}")
        start += 1


for counter in generator(1, 10):
    print(f"counter = {counter}")
