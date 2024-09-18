def is_prime(num):
    """
    Determines if a given number is a prime number.

    Args:
    num (int): The number to be checked.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    # Handle edge cases for numbers less than 2
    if num <= 1:
        return False
    if num == 2:  # 2 is the smallest prime number
        return True

    # Only check for factors up to the square root of num
    # If a number n has a divisor larger than sqrt(n),
    # the corresponding divisor will be smaller than sqrt(n)
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:  # If divisible by any number, it's not prime
            return False

    return True  # Return True if no divisors are found
