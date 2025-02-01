from typing import Any


def one_seven_two(data: list[Any], count: int):
    """Write a Python program to remove the last N number of elements from a given list."""
    return data[: count * -1]


print(one_seven_two([2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5], 3))
assert one_seven_two([2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5], 3) == [
    2,
    3,
    9,
    8,
    2,
    0,
    39,
    84,
    2,
    2,
    34,
    2,
    34,
]
assert one_seven_two([2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5], 5) == [
    2,
    3,
    9,
    8,
    2,
    0,
    39,
    84,
    2,
    2,
    34,
]
assert one_seven_two([2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5], 1) == [
    2,
    3,
    9,
    8,
    2,
    0,
    39,
    84,
    2,
    2,
    34,
    2,
    34,
    5,
    3,
]


def one_seven_three(data: list[str], start: int, end: int):
    """Write a Python program to merge some list items in a given list using the index value."""
    return data[:start] + ["".join(data[start:end])] + data[end:]


print(one_seven_three(["a", "b", "c", "d", "e", "f", "g"], 2, 4))
assert one_seven_three(["a", "b", "c", "d", "e", "f", "g"], 2, 4) == [
    "a",
    "b",
    "cd",
    "e",
    "f",
    "g",
]
assert one_seven_three(["a", "b", "c", "d", "e", "f", "g"], 3, 7) == [
    "a",
    "b",
    "c",
    "defg",
]
