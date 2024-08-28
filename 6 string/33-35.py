def thirty_three(number, width):
    """
    Write a Python program to print the following integers with zeros to the left of the specified
    width.
    """
    return str(number).zfill(width)


print(thirty_three(3, 2))
assert thirty_three(3, 2) == "03"
assert thirty_three(123, 6) == "000123"


def thirty_four(number, width):
    """
    Write a Python program to print the following integers with '*' to the right of the specified
    width.
    """
    return str(number).ljust(width, "*")


print(thirty_four(3, 2))
assert thirty_four(3, 2) == "3*"
assert thirty_four(123, 6) == "123***"


def thirty_two(number):
    """Write a Python program to display a number with a comma separator."""
    return f"{number:,}"


print(thirty_two(3000000))
assert thirty_two(3000000) == "3,000,000"
assert thirty_two(30000000) == "30,000,000"
