from math import ceil
from typing import Any


def one_six_five(data: list[Any], size: int):
    """
    Write a Python program to check if a given list increases strictly. Moreover, if removing only
    one element from the list results in a strictly increasing list, we still consider the list
    true.
    """
    return [data[(i * size) : ((i + 1) * size)] for i in range(ceil(len(data) / size))]


print(one_six_five([12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83], 3))
assert one_six_five(
    [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83], 3
) == [[12, 45, 23], [67, 78, 90], [45, 32, 100], [76, 38, 62], [73, 29, 83]]
assert one_six_five(
    [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83], 4
) == [[12, 45, 23, 67], [78, 90, 45, 32], [100, 76, 38, 62], [73, 29, 83]]
assert one_six_five(
    [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83], 5
) == [[12, 45, 23, 67, 78], [90, 45, 32, 100, 76], [38, 62, 73, 29, 83]]


def one_six_six(data: list[Any]):
    """Write a Python program to remove None value from a given list."""
    return [item for item in data if item is not None]


print(one_six_six([12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]))
assert one_six_six([12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]) == [
    12,
    0,
    23,
    -55,
    234,
    89,
    0,
    6,
    -12,
]


def one_six_seven(data: list[str]):
    """Write a Python program to convert a given list of strings into list of lists."""
    return list(map(list, data))


print(one_six_seven(["Red", "Maroon", "Yellow", "Olive"]))
assert one_six_seven(["Red", "Maroon", "Yellow", "Olive"]) == [
    ["R", "e", "d"],
    ["M", "a", "r", "o", "o", "n"],
    ["Y", "e", "l", "l", "o", "w"],
    ["O", "l", "i", "v", "e"],
]
