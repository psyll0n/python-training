def filter_even_numbers(num):
    """
    Returns only even numbers.
    """
    return num % 2 == 0


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for num in filter(filter_even_numbers, nums):
    print(num)


evens = list(filter(filter_even_numbers, nums))
