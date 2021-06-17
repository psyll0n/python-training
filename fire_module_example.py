#!/usr/bin/env python3

"""
Simple fire module example...
"""

import fire


def greet(greeting="Hiya", name="Tammy"):
    print(f"{greeting} {name}")


def goodbye(goodbye="Bye", name="Tammy"):
    print(f"{goodbye} {name}")


if __name__ == "__main__":
    fire.Fire()
