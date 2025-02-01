from typing import Any


def one_zero_eight(data: list[Any], column: int):
    """Write a Python program to extract a specified column from a given nested list."""
    return [sublist[column - 1] for sublist in data]


print(one_zero_eight([[1, 2, 3], [2, 4, 5], [1, 1, 1]], 1))
assert one_zero_eight([[1, 2, 3], [2, 4, 5], [1, 1, 1]], 1) == [1, 2, 1]
assert one_zero_eight([[1, 2, 3], [-2, 4, -5], [1, -1, 1]], 3) == [3, -5, 1]


def one_zero_nine(data: list[Any], shift: int):
    """
    Write a Python program to rotate a given list by a specified number of items in the right or
    left direction.
    """
    return data[shift:] + data[:shift]


print(one_zero_nine([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4))
assert one_zero_nine([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4) == [
    5,
    6,
    7,
    8,
    9,
    10,
    1,
    2,
    3,
    4,
]
assert one_zero_nine([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2) == [
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    1,
    2,
]
assert one_zero_nine([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -4) == [
    7,
    8,
    9,
    10,
    1,
    2,
    3,
    4,
    5,
    6,
]
assert one_zero_nine([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -2) == [
    9,
    10,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
]


def one_one_zero(data: list[Any]):
    """Write a Python program to find the item with maximum occurrences in a given list."""
    counts = {}
    for item in data:
        if item not in counts:
            counts[item] = 0
        counts[item] += 1
    return sorted(counts.items(), key=lambda item: item[1], reverse=True)[0][0]


print(one_one_zero([2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]))
assert one_one_zero([2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]) == 2
