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


def add(*args):
    total = 0
    for num in args:
        total += num
    print(f"The total is: {total}")


add(2, 43, 53, 76, 80)


# The call to the main function below allows script-like execution of the code
if __name__ == "__main__":
    main()
