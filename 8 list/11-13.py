from typing import Any


def one_one(one: list[Any], two: list[Any]):
    """
    Write a Python function that takes two lists and returns True if they have at least one common
    member.
    """
    return any(item in two for item in one)


print(one_one([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
assert one_one([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]) is True
assert one_one([1, 2, 3, 4, 5], [6, 7, 8, 9]) is False


def one_two(data: list[Any]):
    """
    Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
    """
    del data[5]
    del data[4]
    del data[0]
    return data


print(one_two(["Red", "Green", "White", "Black", "Pink", "Yellow"]))
assert one_two(["Red", "Green", "White", "Black", "Pink", "Yellow"]) == [
    "Green",
    "White",
    "Black",
]


def one_three():
    """Write a Python program to generate a 3*4*6 3D array whose each element is *."""
    return [[["*" for _ in range(6)] for _ in range(4)] for _ in range(3)]


print(one_three())
assert one_three() == [
    [
        ["*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*"],
    ],
    [
        ["*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*"],
    ],
    [
        ["*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*"],
        ["*", "*", "*", "*", "*", "*"],
    ],
]
