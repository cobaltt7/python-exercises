from itertools import count
from typing import Any


def five_three():
    """Write a Python program to create a list with infinite elements."""
    return count()


print(five_three())


def five_four(data: list[str], character=""):
    """Write a Python program to concatenate elements of a list."""
    return character.join(data)


print(five_four(["red", "green", "orange"], "-"))
assert five_four(["red", "green", "orange"], "-") == "red-green-orange"
assert five_four(["red", "green", "orange"]) == "redgreenorange"


def five_five(data: list[dict[str, Any]]):
    """Write a Python program to calculate the difference between the two lists."""
    return [
        {key: value for key, value in item.items() if key != "key1"} for item in data
    ]


print(
    five_five(
        [{"key1": "value1", "key2": "value2"}, {"key1": "value3", "key2": "value4"}]
    )
)
assert five_five(
    [{"key1": "value1", "key2": "value2"}, {"key1": "value3", "key2": "value4"}]
) == [{"key2": "value2"}, {"key2": "value4"}]
