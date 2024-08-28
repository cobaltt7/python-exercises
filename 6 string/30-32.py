def thirty(number):
    """Write a Python program to print the following numbers up to 2 decimal places."""
    return "{:.2f}".format(number)


print(thirty(3.1415926))
assert thirty(3.1415926) == "3.14"
assert thirty(12.9999) == "13.00"


def thirty_one(number):
    """Write a Python program to print the following numbers up to 2 decimal places with a sign."""
    return "{:+.2f}".format(number)


print(thirty_one(3.1415926))
assert thirty_one(3.1415926) == "+3.14"
assert thirty_one(-12.9999) == "-13.00"


def thirty_two(number):
    """
    Write a Python program to print the following positive and negative numbers with no decimal places.
    """
    return "{:.0f}".format(number)


print(thirty_two(3.1415926))
assert thirty_two(3.1415926) == "3"
assert thirty_two(-12.9999) == "-13"
