from operator import concat
from random import randint
from typing import Any


def fourteen(data: list[Any]):
    """
    Write a Python program to print the numbers of a specified list after removing even numbers from
    it.
    """
    return [number for number in data if number % 2]


print(fourteen([7, 8, 120, 25, 44, 20, 27]))
assert fourteen([7, 8, 120, 25, 44, 20, 27]) == [7, 25, 27]


def fifteen(data: list[Any]):
    """Write a Python program to shuffle and print a specified list."""
    return sorted(data, key=lambda _: randint(1, 100))


print(fifteen(["Red", "Green", "White", "Black", "Pink", "Yellow"]))


def sixteen():
    """
    Write a Python program to generate and print a list of the first and last 5 elements where the
    values are square numbers between 1 and 30 (both included).
    """
    return concat(
        [number**2 for number in range(1, 6)], [number**2 for number in range(26, 31)]
    )


print(sixteen())
assert sixteen() == [1, 4, 9, 16, 25, 676, 729, 784, 841, 900]
