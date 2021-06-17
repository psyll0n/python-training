# The function below removes the first and last character of a given string.

print("This scrip removes the first and last character of a given string.")

string = input("Enter a string: ")


def stringManipulation(string):
    return string[1 : len(string) - 1]


print(stringManipulation(string))
