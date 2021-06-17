# The function called repeatStr repeats a given string string exactly x times.

x = int(input("Enter a number: "))
string = input("Enter a string: ")


def repeatStr(string):
    return string * x


print(repeatStr(string))
