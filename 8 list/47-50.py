from json import dumps
from typing import Any


def four_seven(data: list[Any], new: Any):
    """Write a Python program to insert an element before each element of a list."""
    output = []
    for item in data:
        output.append(new)
        output.append(item)
    return output


print(four_seven(["Red", "Green", "Black"], "c"))
assert four_seven(["Red", "Green", "Black"], "c") == [
    "c",
    "Red",
    "c",
    "Green",
    "c",
    "Black",
]


def four_eight(data: list[list[Any]]):
    """
    Write a Python program to print a nested lists (each list on a new line) using the print()
    function.
    """
    return "\n".join(dumps(a) for a in data)


print(four_eight([["Red"], ["Green"], ["Black"]]))
assert (
    four_eight([["Red"], ["Green"], ["Black"]])
    == """["Red"]
["Green"]
["Black"]"""
)


def four_nine(names: list[str], codes: list[str]):
    """Write a Python program to convert list to list of dictionaries."""
    return [
        {"color_name": name, "color_code": codes[index]}
        for index, name in enumerate(names)
    ]


print(
    four_nine(
        ["Black", "Red", "Maroon", "Yellow"],
        ["#000000", "#FF0000", "#800000", "#FFFF00"],
    )
)
assert four_nine(
    ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
) == [
    {"color_name": "Black", "color_code": "#000000"},
    {"color_name": "Red", "color_code": "#FF0000"},
    {"color_name": "Maroon", "color_code": "#800000"},
    {"color_name": "Yellow", "color_code": "#FFFF00"},
]


def five_zero(data: list[Any]):
    """Write a Python program to sort a list of nested dictionaries."""
    return sorted(data, key=lambda item: item["key"]["subkey"], reverse=True)


print(
    five_zero([{"key": {"subkey": 1}}, {"key": {"subkey": 10}}, {"key": {"subkey": 5}}])
)
assert five_zero(
    [{"key": {"subkey": 1}}, {"key": {"subkey": 10}}, {"key": {"subkey": 5}}]
) == [{"key": {"subkey": 10}}, {"key": {"subkey": 5}}, {"key": {"subkey": 1}}]
