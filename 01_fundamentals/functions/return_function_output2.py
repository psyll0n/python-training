#! python3


def function_1(text):
    return text + " " + text


def function_2(text):
    return text.title()


# Use the output of function_1 as input of function_2.
# Store that in the `output` variable.
output = function_2(function_1("hello"))
print(output)


def outer_function(a, b):
    def inner_function(c, d):
        return c + d

    # The output of inner_function becomes the output of outer_function.
    return inner_function(a, b)


result = outer_function(5, 10)

print(result)
