#! python3

def is_leap_year(year):
    """
    Determine whether a given year is a leap year.

    A leap year occurs:
    - Every year that is divisible by 4.
    - Except for years that are divisible by 100, which are not leap years.
    - However, years divisible by 400 are leap years.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.

    Examples:
        >>> is_leap_year(2000)
        True
        >>> is_leap_year(2100)
        False
        >>> is_leap_year(2024)
        True
        >>> is_leap_year(2023)
        False
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # Divisible by 400 -> Leap year
            else:
                return False  # Divisible by 100 but not 400 -> Not a leap year
        else:
            return True  # Divisible by 4 but not by 100 -> Leap year
    else:
        return False  # Not divisible by 4 -> Not a leap year


print(is_leap_year(int(input("Specify a year: "))))