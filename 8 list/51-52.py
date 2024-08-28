from math import ceil
from typing import Any


def five_one(data: list[Any], n: int):
    """Write a Python program to split a list every Nth element."""
    output = []
    length = len(data)
    count = ceil(length / n)
    for index in range(count):
        start = index * n
        output.append(data[start : min(length, start + n)])
    return output


print(
    five_one(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"], 3)
)
assert five_one(
    ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"], 3
) == [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"],
    ["j", "k", "l"],
    ["m", "n"],
]


def five_two(one: list[Any], two: list[Any]):
    """Write a Python program to calculate the difference between the two lists."""
    return [[x for x in one if x not in two], [x for x in two if x not in one]]


print(five_two([1, 3, 5, 7, 9], [1, 2, 4, 6, 7, 8]))
assert five_two([1, 3, 5, 7, 9], [1, 2, 4, 6, 7, 8]) == [[3, 5, 9], [2, 4, 6, 8]]
assert five_two(
    ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
) == [["red", "orange", "white"], ["black", "yellow"]]
