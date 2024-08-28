def six(number):
    """Write a Python program to get the sum of a non-negative integer."""
    number = str(number)
    return int(number[0]) + six(number[1:]) if len(number) else 0


print(six(345))
assert six(345) == 12
assert six(45) == 9


def seven(number, x=0):
    """
    Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)...
    (until n-x =< 0).
    """
    return number - x + seven(number, x + 2) if number > x else 0


print(seven(6))
assert seven(6) == 12
assert seven(10) == 30


def eight(index):
    """
    Write a Python program to calculate the harmonic sum of n-1.

    Note: The harmonic sum is the sum of reciprocals of the positive integers.

    Example:
        1 + 1/2 + 1/3 + 1/4 + 1/5 + ....
    """
    return 0 if index == 0 else 1 / index + eight(index - 1)


print(eight(7))
assert eight(7) == 2.5928571428571425
assert eight(4) == 2.083333333333333
