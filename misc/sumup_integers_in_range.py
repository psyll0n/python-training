# Given two integers a and b, which can be positive or negative, find the sum of all the
# integers between including them too and return it. If the two numbers are equal return a or b.

a = int(input("Enter a number for a: "))
b = int(input("Enter a number for b: "))


def get_sum(a, b):
    return sum(range(min(a, b), max(a, b) + 1))


print(get_sum(a, b))
