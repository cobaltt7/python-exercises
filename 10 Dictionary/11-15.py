from math import prod
from typing import Any, Hashable, OrderedDict


def eleven(data: dict[Hashable, float]):
    """Write a Python program to multiply all the items in a dictionary."""
    return prod(data.values())


print(eleven({"data1": 100, "data2": -54, "data3": 247}))
assert eleven({"data1": 100, "data2": -54, "data3": 247}) == -1333800


def tweleve(data: dict[Hashable, Any], search: Hashable):
    """Write a Python program to remove a key from a dictionary."""
    return dict((key, value) for key, value in data.items() if key != search)


print(tweleve({"a": 1, "b": 2, "c": 3, "d": 4}, "a"))
assert tweleve({"a": 1, "b": 2, "c": 3, "d": 4}, "a") == {"b": 2, "c": 3, "d": 4}


def thirteen(keys: list[Hashable], values: list[Any]):
    """Write a Python program to map two lists into a dictionary."""
    return dict(zip(keys, values))


print(thirteen(["red", "green", "blue"], ["#FF0000", "#008000", "#0000FF"]))
assert thirteen(["red", "green", "blue"], ["#FF0000", "#008000", "#0000FF"]) == {
    "red": "#FF0000",
    "green": "#008000",
    "blue": "#0000FF",
}


def fourteen(data: dict[str, Any]):
    """Write a Python program to sort a dictionary by key."""
    output = OrderedDict()
    for key, value in sorted(data.items(), key=lambda entry: entry[0]):
        output[key] = value
    return output


print(
    fourteen(
        {"red": "#FF0000", "green": "#008000", "black": "#000000", "white": "#FFFFFF"}
    )
)
assert fourteen(
    {"red": "#FF0000", "green": "#008000", "black": "#000000", "white": "#FFFFFF"}
) == OrderedDict(
    {"black": "#000000", "green": "#008000", "red": "#FF0000", "white": "#FFFFFF"}
)
assert fourteen(
    {"name1": "Theodore", "name2": "Mathew", "name4": "Roxanne", "name3": "David"}
) == OrderedDict(
    {"name1": "Theodore", "name2": "Mathew", "name3": "David", "name4": "Roxanne"}
)


def fifteen(data: dict[Hashable, float]):
    """Write a Python program to get the maximum and minimum value in a dictionary."""
    values = data.values()
    return (max(values), min(values))


print(fifteen({"x": 500, "y": 5874, "z": 560}))
assert fifteen({"x": 500, "y": 5874, "z": 560}) == (5874, 500)
