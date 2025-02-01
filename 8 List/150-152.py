from heapq import merge
from typing import Any


def one_five_zero(data: list[list[Any]]):
    """Write a Python program to reverse a given list of lists."""
    return data[::-1]


print(one_five_zero([["orange", "red"], ["green", "blue"], ["white", "black", "pink"]]))
assert one_five_zero(
    [["orange", "red"], ["green", "blue"], ["white", "black", "pink"]]
) == [["white", "black", "pink"], ["green", "blue"], ["orange", "red"]]
assert one_five_zero([[1, 2, 3, 4], [0, 2, 4, 5], [2, 3, 4, 2, 4]]) == [
    [2, 3, 4, 2, 4],
    [0, 2, 4, 5],
    [1, 2, 3, 4],
]


def one_five_one(data: list[float], indicies: tuple[int, int]):
    """
    Write a Python program to find the maximum and minimum values in a given list within specified
    index range.
    """
    section = data[indicies[0] : indicies[1]]
    return (max(section), min(section))


print(one_five_one([4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5], (3, 8)))
assert one_five_one([4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5], (3, 8)) == (5, 0)


def one_five_two(one: list[Any], two: list[Any]):
    """Write a Python program to combine two sorted lists using the heapq module."""
    return list(merge(one, two))


print(one_five_two([1, 3, 5, 7, 9, 11], [0, 2, 4, 6, 8, 10]))
assert one_five_two([1, 3, 5, 7, 9, 11], [0, 2, 4, 6, 8, 10]) == [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
]
