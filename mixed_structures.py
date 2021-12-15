#!/usr/bin/env python3


# globals
dlevel = 0  # manage nesting level


def main():
    r = range(11)
    l = list[1, "2", 3, {"four": 4}, 5]
    t = ("one", "two", None, "four", 5)
    s = set("It's a bird! It's a plane! It's a superman!")
    d = dict(one=1, two=2, three=3, four=4, five=5)
    mixed = [r, l, t, s, d]
    display(mixed)


def display(o):
    global dlevel

    dlevel += 1
    if isinstance(o, list):
        print_list(o)
    elif isinstance(o, range):
        print_list(o)
    elif isinstance(o, tuple):
        print_tuple(o)
    elif isinstance(o, set):
        print_set(o)
    elif isinstance(o, dict):
        print_dict(o)
    elif o is None:
        print("Nada", end=" ", flush=True)
    else:
        print(repr(o), end=" ", flush=True)
    dlevel -= 1


def print_list(o):
    print("[", end=" ")
    for x in o:
        display(x)
    print("]", end=" ", flush=True)


def print_tuple(o):
    print("(", end=" ")
    for x in o:
        display(x)
    print(")", end=" ", flush=True)


def print_set(o):
    print("{", end=" ")
    for x in o:
        display(x)
    print("}", end=" ", flush=True)


def print_dict(o):
    print("{", end=" ")
    for k, v in o.items():
        print(k, end=": ")
        display(v)
    print("}", end=" ", flush=True)


if __name__ == "__main__":
    main()
