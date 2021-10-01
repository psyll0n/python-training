#!/usr/bin/env python3


def F1(f):
    print("A")

    def F2():
        print("B")
        f()
        print("C")

    print("D")
    return F2


@F1
def F3():
    print("E")


F3()
