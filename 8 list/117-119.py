from typing import Any


def one_one_seven(one: list[Any], two: list[Any]):
    """
    Write a Python program to remove all elements from a given list that are present in another
    list.
    """
    return [item for item in one if item not in two]


print(one_one_seven([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]))
assert one_one_seven([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [
    1,
    3,
    5,
    7,
    9,
    10,
]


def one_one_eight(data: list[Any]):
    """
    Write a Python program to find the difference between elements (n+1th – nth) of a given list of
    numeric values.
    """
    return [item - data[index - 1] for index, item in list(enumerate(data))[1:]]


print(one_one_eight([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
assert one_one_eight([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 1, 1, 1, 1, 1, 1, 1, 1]
assert one_one_eight([2, 4, 6, 8]) == [2, 2, 2]


def one_one_nine(data: list[Any], substring: str):
    """Write a Python program to check if a substring presents in a given list of string values."""
    return any(substring in item for item in data)


print(one_one_nine(["red", "black", "white", "green", "orange"], "ack"))
assert one_one_nine(["red", "black", "white", "green", "orange"], "ack") is True
assert one_one_nine(["red", "black", "white", "green", "orange"], "abc") is False
