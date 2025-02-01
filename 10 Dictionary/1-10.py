from collections import OrderedDict
from operator import itemgetter
from typing import Any, Hashable


def one(data: dict):
    """
    Write a Python program to sort (ascending and descending) a dictionary by value.
    """
    entries = data.items()
    ascending = OrderedDict(sorted(entries, key=itemgetter(1)))
    descending = OrderedDict(sorted(entries, key=itemgetter(1), reverse=True))
    return (ascending, descending)


print(one({1: 2, 3: 4, 4: 3, 2: 1, 0: 0}))
assert one({1: 2, 3: 4, 4: 3, 2: 1, 0: 0}) == (
    OrderedDict([(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]),
    OrderedDict([(3, 4), (4, 3), (1, 2), (2, 1), (0, 0)]),
)


def two(data: dict, key: Hashable, value: Any):
    """Write a Python program to add a key to a dictionary."""
    return {**data, key: value}


print(two({0: 10, 1: 20}, 2, 30))
assert two({0: 10, 1: 20}, 2, 30) == {0: 10, 1: 20, 2: 30}


def three(data: list[dict]):
    """
    Write a Python program to concatenate following dictionaries to create a new one.
    """
    output: dict = {}
    for subdict in data:
        output = {**output, **subdict}
    return output


print(three([{1: 10, 2: 20}, {3: 30, 4: 40}, {5: 50, 6: 60}]))
assert three([{1: 10, 2: 20}, {3: 30, 4: 40}, {5: 50, 6: 60}]) == {
    1: 10,
    2: 20,
    3: 30,
    4: 40,
    5: 50,
    6: 60,
}


def four(data: dict, key: Hashable):
    """
    Write a Python program to check if a given key already exists in a dictionary.
    """
    return key in data


print(four({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}, 5))
assert four({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}, 5) is True
assert four({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}, 9) is False


def five(data: dict):
    """Write a Python program to iterate over dictionaries using for loops."""
    output = ""
    for key, value in data.items():
        output += f"{key} -> {value}\n"
    return output


print(five({"x": 10, "y": 20, "z": 30}))
assert five({"x": 10, "y": 20, "z": 30}) == """x -> 10
y -> 20
z -> 30
"""


def six(limit: int):
    """
    Write a Python script to generate and print a dictionary that contains a number
    (between 1 and n) in the form (x, x*x).
    """
    output: dict[int, int] = {}
    for number in range(1, limit + 1):
        output[number] = number**2
    return output


print(six(10))
assert six(10) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


def seven() -> dict[int, int]:
    """
    Write a Python script to print a dictionary where the keys are numbers between 1
    and 15 (both included) and the values are square of keys.
    """
    output: dict[int, int] = {}
    for number in range(1, 16):
        output[number] = number**2
    return output


print(seven())
assert seven() == {
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25,
    6: 36,
    7: 49,
    8: 64,
    9: 81,
    10: 100,
    11: 121,
    12: 144,
    13: 169,
    14: 196,
    15: 225,
}


def eight(data: list[dict]):
    """Write a Python script to merge two Python dictionaries."""
    output: dict = {}
    for subdict in data:
        output = {**output, **subdict}
    return output


print(eight([{"a": 100, "b": 200}, {"x": 300, "y": 200}]))
assert eight([{"a": 100, "b": 200}, {"x": 300, "y": 200}]) == {
    "x": 300,
    "y": 200,
    "a": 100,
    "b": 200,
}


def nine(data: dict):
    """Write a Python program to iterate over dictionaries using for loops."""
    output = ""
    for key, value in data.items():
        output += f"{key} corresponds to {value}\n"
    return output


print(nine({"Red": 1, "Green": 2, "Blue": 3}))
assert nine({"Red": 1, "Green": 2, "Blue": 3}) == """Red corresponds to 1
Green corresponds to 2
Blue corresponds to 3
"""


def ten(data: dict[Hashable, float]):
    """Write a Python program to sum all the items in a dictionary."""
    return sum(data.values())


print(ten({"data1": 100, "data2": -54, "data3": 247}))
assert ten({"data1": 100, "data2": -54, "data3": 247}) == 293
