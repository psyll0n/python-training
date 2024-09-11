#!/usr/bin/env python3
# multihreadDemo.py - Multi-threading example.

import threading, time

print("Start of program.")


def takeANap():
    time.sleep(5)
    print("Wake up!")
    print("Wake up!")
    print("Wake up!")


threadObj = threading.Thread(target=takeANap)
threadObj.start()


print("End of program.")
