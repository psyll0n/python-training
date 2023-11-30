from cs50 import get_int


def main():
    height = get_height()
    for i in range(height):
        print("#")


def get_height():
    while True:
        try:
            n = get_int("Height: ")
            if n > 0:
                return n
        except ValueError:
            print("Not an integer..")


main()
