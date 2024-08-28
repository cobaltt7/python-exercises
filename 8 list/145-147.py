from random import choice
from typing import Any


def one_four_five(bounds: tuple[int, int], exclude: list[int] | None = None):
    """
    Write a Python program to generate a number in a specified range except some specific numbers.
    """
    return choice(
        [number for number in range(*bounds) if number not in (exclude or [])]
    )


print(one_four_five((1, 10), [2, 9, 10]))
print(one_four_five((-5, 5), [-5, 0, 4, 3, 2]))


def one_four_six(data: list[float | str]):
    """Write a Python program to compute the sum of digits of each number of a given list."""
    return sum(
        sum(int(digit) for digit in str(item) if digit.isdigit()) for item in data
    )


print(one_four_six([10, 2, 56]))
assert one_four_six([10, 2, 56]) == 14
assert one_four_six([10, 20, 4, 5, "b", 70, "a"]) == 19
assert one_four_six([10, 20, -4, 5, -70]) == 19
