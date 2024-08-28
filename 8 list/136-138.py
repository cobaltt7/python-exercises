from typing import Any


def one_three_six(data: list[Any]):
    """Write a Python program to remove duplicate words from a given list of strings."""
    return [item for index, item in enumerate(data) if index == data.index(item)]


print(one_three_six(["Python", "Exercises", "Practice", "Solution", "Exercises"]))
assert one_three_six(["Python", "Exercises", "Practice", "Solution", "Exercises"]) == [
    "Python",
    "Exercises",
    "Practice",
    "Solution",
]


def one_three_four(data: list[int]):
    """Write a Python program to find a first even and odd number in a given list of numbers."""
    return (
        next(item for item in data if item % 2 == 0),
        next(item for item in data if item % 2 == 1),
    )


print(one_three_four([1, 3, 5, 7, 4, 1, 6, 8]))
assert one_three_four([1, 3, 5, 7, 4, 1, 6, 8]) == (4, 1)


def one_three_five(data: list[float | str]):
    """
    Write a Python program to sort a given mixed list of integers and strings. Numbers must be
    sorted before strings.
    """
    numbers = sorted(item for item in data if isinstance(item, (int, float)))
    strings = sorted(item for item in data if isinstance(item, str))
    return [*numbers, *strings]


print(one_three_five([19, "red", 12, "green", "blue", 10, "white", "green", 1]))
assert one_three_five([19, "red", 12, "green", "blue", 10, "white", "green", 1]) == [
    1,
    10,
    12,
    19,
    "blue",
    "green",
    "green",
    "red",
    "white",
]
