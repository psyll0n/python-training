# Mapping example in Python

nums = [1, -5, 7.25, 99]

for num in nums:
    print(num * 4)


new_nums = [num * 4 for num in nums]

new_nums


def new_func(num):
    if num > 5:
        num = num + 4
    else:
        num = num - 4

    return num ** 2


nums

for new_nums in map(new_func, nums):
    print(new_nums)
