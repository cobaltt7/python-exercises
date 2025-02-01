from math import floor
from typing import Any, Tuple


def forty_four(data: list[Any]):
    """Write a Python program to generate groups of five consecutive numbers in a list."""
    count = floor(len(data) / 5)
    return [data[index * 5 : ((index + 1) * 5)] for index in range(count)]


print(forty_four([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
assert forty_four([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]
assert forty_four([
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
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
]) == [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]


def forty_five(data: list[Tuple[float, float]]):
    """Write a Python program to convert a pair of values into a sorted unique array."""
    return sorted(set(item for sublist in data for item in sublist))


print(
    forty_five([
        (1, 2),
        (3, 4),
        (1, 2),
        (5, 6),
        (7, 8),
        (1, 2),
        (3, 4),
        (3, 4),
        (7, 8),
        (9, 10),
    ])
)
assert forty_five(
    [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)]
) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def forty_six(data: list[int]):
    """Write a Python program to select the odd items of a list."""
    return [number for number in data if number % 2]


print(forty_six([1, 2, 3, 4, 5, 6, 7, 8, 9]))
assert forty_six([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 3, 5, 7, 9]
