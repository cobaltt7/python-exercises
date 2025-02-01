from typing import Any, Callable, Union
from math import floor
from random import random


def two_one_nine(callback: Callable, seed: Any):
    """
    Write a Python program to build a list, using an iterator function and an initial seed value.
    """
    output = []
    value = callback(seed)
    while value:
        item, next_seed = value
        output.append(item)
        value = callback(next_seed)
    return output


print(two_one_nine(lambda n: False if n > 40 else [-n, n + 10], 10))
assert (two_one_nine(lambda n: False if n > 40 else [-n, n + 10], 10)) == [
    -10,
    -20,
    -30,
    -40,
]


def two_two_zero(data: list[Any], callback: Callable):
    """
    Write a Python program to map the values of a list to a dictionary using a function, where the
    key-value pairs consist of the original value as the key and the result of the function as the
    value.
    """
    return dict(zip(data, map(callback, data)))


print(two_two_zero([1, 2, 3], lambda x: x * x))
assert (two_two_zero([1, 2, 3], lambda x: x * x)) == {1: 1, 2: 4, 3: 9}


def two_two_one(data: list[Any]):
    """
    Write a Python program to randomize the order of the values of an list, returning a new list.
    """
    return sorted(data, key=lambda _: random())


print(two_two_one([1, 2, 3, 4, 5, 6]))


def two_two_two(one: list[Any], two: list[Any], callback: Callable):
    """
    Write a Python program to get the difference between two given lists, after applying the
    provided function to each list element of both.
    """
    search_array = set(map(callback, two))
    output = []
    for item in one:
        if not callback(item) in search_array:
            output.append(item)
    return output


print(two_two_two([{"x": 2}, {"x": 1}], [{"x": 1}], lambda v: v["x"]))
assert (two_two_two([2.1, 1.2], [2.3, 3.4], floor)) == [1.2]
assert (two_two_two([{"x": 2}, {"x": 1}], [{"x": 1}], lambda v: v["x"])) == [{"x": 2}]


def two_two_three(data: list[Any]):
    """Write a Python program to create a list with the non-unique values filtered out."""
    output: list[Any] = []
    for item in data:
        if item in output:
            output.remove(item)
        else:
            output.append(item)
    return output


print(two_two_three([1, 2, 2, 3, 4, 4, 5]))
assert (two_two_three([1, 2, 2, 3, 4, 4, 5])) == [1, 3, 5]


def two_two_four(data: list[Any]):
    """Write a Python program to create a list with the unique values filtered out."""
    seen = set()
    output = []
    for item in data:
        if item in seen and item not in output:
            output.append(item)
        else:
            seen.add(item)
    return output


print(two_two_four([1, 2, 2, 3, 4, 4, 5]))
assert (two_two_four([1, 2, 2, 3, 4, 4, 5])) == [2, 4]


def two_two_five(data: Any, keys: list[Union[int, str]]):
    """
    Write a Python program to retrieve the value of the nested key indicated by the given selector
    list from a dictionary or list.
    """
    output = data
    for key in keys:
        output = output[key]
    return output


print(
    two_two_five(
        {
            "freddy": {
                "name": {"first": "Fateh", "last": "Harwood"},
                "postIds": [1, 2, 3],
            }
        },
        ["freddy", "name", "last"],
    )
)
assert (
    two_two_five(
        {
            "freddy": {
                "name": {"first": "Fateh", "last": "Harwood"},
                "postIds": [1, 2, 3],
            }
        },
        ["freddy", "name", "last"],
    )
) == "Harwood"
assert (
    two_two_five(
        {
            "freddy": {
                "name": {"first": "Fateh", "last": "Harwood"},
                "postIds": [1, 2, 3],
            }
        },
        ["freddy", "postIds", 1],
    )
) == 2
