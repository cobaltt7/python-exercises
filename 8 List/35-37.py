from typing import Any


def three_five(data: list[str], num: int):
    """
    Write a Python program to create a list by concatenating a given list with a range from 1 to n.
    """
    extended = data * num
    length = len(data)
    return [f"{item}{index//length + 1}" for index, item in enumerate(extended)]


print(three_five(["p", "q"], 5))
assert three_five(["p", "q"], 5) == [
    "p1",
    "q1",
    "p2",
    "q2",
    "p3",
    "q3",
    "p4",
    "q4",
    "p5",
    "q5",
]


def three_six(data: Any):
    """Write a Python program to get a variable with an identification number or string."""
    return f"{id(data):x}"


print(three_six([10, 20, 30, 40]))
print(three_six(100))
print(three_six("w3resource"))


def three_seven(one: list[Any], two: list[Any]):
    """Write a Python program to find common items in two lists."""
    return [x for x in one if x in two]


print(
    three_seven(
        ["Red", "Green", "Orange", "White"], ["Black", "Green", "White", "Pink"]
    )
)
assert three_seven(
    ["Red", "Green", "Orange", "White"], ["Black", "Green", "White", "Pink"]
) == ["Green", "White"]
