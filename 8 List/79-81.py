import random
from typing import Any


def seven_nine(data: list[Any], index: int):
    """Write a Python program to remove the K'th element from a given list, print the new list."""
    return data[: index - 1] + data[index:]


print(seven_nine([1, 1, 2, 3, 4, 4, 5, 1], 3))
assert seven_nine([1, 1, 2, 3, 4, 4, 5, 1], 3) == [1, 1, 3, 4, 4, 5, 1]


def eight_zero(data: list[Any], item: Any, index: int):
    """Write a Python program to insert an element at a specified position into a given list."""
    return data[: index - 1] + [item] + data[index - 1 :]


print(eight_zero([1, 1, 2, 3, 4, 4, 5, 1], 12, 3))
assert eight_zero([1, 1, 2, 3, 4, 4, 5, 1], 12, 3) == [1, 1, 12, 2, 3, 4, 4, 5, 1]


def eight_one(data: list[Any], count: int):
    """
    Write a Python program to extract a given number of randomly selected elements from a given list.
    """
    if count == 0:
        return []
    index = random.randint(0, len(data) - 1)
    return [data[index], *eight_one(data[: index - 1] + data[index:], count - 1)]


print(eight_one([1, 1, 2, 3, 4, 4, 5, 1], 3))
