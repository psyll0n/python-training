#!/usr/bin/env python3


def main():
    x = ("meow", "grrr", "purr")
    kitten(*x)


def kitten(*args):
    if len(args):
        for i in args:
            print(i)
    else:
        print("Meow.")


if __name__ == "__main__":
    main()
