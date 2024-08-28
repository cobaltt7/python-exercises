from random import choice
from typing import Any


def twenty_two(data: list[Any], item: Any):
    """
    Write a Python program to find the index of an item in a specified list.
    """
    for index, found in enumerate(data):
        if found == item:
            return index
    return None


print(twenty_two([10, 30, 4, -6], 30))
assert twenty_two([10, 30, 4, -6], 30) == 1


def twenty_three(data: list[list[Any]]):
    """Write a Python program to flatten a shallow list."""
    return [item for sublist in data for item in sublist]


print(twenty_three([[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]))
assert twenty_three([[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]) == [
    2,
    4,
    3,
    1,
    5,
    6,
    9,
    7,
    9,
    0,
]


def twenty_four(one: list[Any], two: list[Any]):
    """Write a Python program to append a list to the second list."""
    return one + two


print(twenty_four([1, 2, 3, 0], ["Red", "Green", "Black"]))
assert twenty_four([1, 2, 3, 0], ["Red", "Green", "Black"]) == [
    1,
    2,
    3,
    0,
    "Red",
    "Green",
    "Black",
]


def twenty_five(data: list[Any]):
    """Write a Python program to select an item randomly from a list."""
    return data[choice(range(len(data)))]


print(twenty_five(["Red", "Blue", "Green", "White", "Black"]))
