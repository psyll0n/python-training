import sys

names = ["Bill", "Charlie", "Fred", "George", "Ginny", "Percy", "Ron"]

name = input("Name: ")

for n in names:
    if name == n:
        print("Name found...")
        sys.exit()


print("Name not found...")
sys.exit(1)
