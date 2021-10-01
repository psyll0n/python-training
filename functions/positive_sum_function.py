# A function that returns the sum of all positive numbers in a list.
def positive_sum(arr):
    x = 0
    for i in arr:
        if i > 0:
            x += i
    return x


print(
    positive_sum(
        [
            81,
            42,
            -58,
            -97,
            -70,
            49,
            52,
            -11,
            24,
            -20,
            17,
            -1,
            96,
            -8,
            -37,
            45,
            14,
            40,
            43,
            -82,
            77,
            93,
            -11,
            42,
            -49,
            -59,
        ]
    )
)
