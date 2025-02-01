from random import random
from typing import Any


def nine_eight(data: list[str]):
    """Write a Python program to scramble the letters of a string in a given list."""
    return ["".join(sorted(sublist, key=lambda _: random())) for sublist in data]


print(nine_eight(["Python", "list", "exercises", "practice", "solution"]))


def nine_nine(data: list[float | str]):
    """
    Write a Python program to find the maximum and minimum values in a given heterogeneous list.
    """
    numbers = [item for item in data if isinstance(item, (float, int))]
    return sorted(numbers)[-1 :: -1 * (len(numbers) - 1)]


print(nine_nine(["Python", 3, 2, 4, 5, "version"]))
assert nine_nine(["Python", 3, 2, 4, 5, "version"]) == [5, 2]


def one_zero_zero(lists: list[list[Any]]):
    """Write a Python program to extract common index elements from more than one given list."""
    return [
        item
        for index, item in enumerate(sorted(lists, key=len)[0])
        if all(list[index] == item for list in lists)
    ]


print(
    one_zero_zero([[1, 1, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 7], [0, 1, 2, 3, 4, 5, 7]])
)
assert one_zero_zero(
    [[1, 1, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 7], [0, 1, 2, 3, 4, 5, 7]]
) == [1, 7]
assert one_zero_zero([[0, 1, 2, 3, 4, 5, 7], [2, 1, 3, 3, 4, 5, 7]]) == [1, 3, 4, 5, 7]
