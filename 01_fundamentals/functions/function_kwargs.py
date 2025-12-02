#!/usr/bin/env python3


def main():
    x = dict(Buffy="meow", Angel="rawr", Zilla="grr")
    kitten(**x)


def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print("Kitten {} says {}".format(k, kwargs[k]))
    else:
        print("Meow.")


if __name__ == "__main__":
    main()
