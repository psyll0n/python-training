#!/usr/bin/env python3
# recursion_function2.py


def countdown(x):
    if x == 0:
        print("Done!")
        return
    else:
        print(x, "...")
        countdown( x - 1 )
        
countdown(10)


