from random import shuffle
from typing import Any


def one_four_seven(one: list[Any], two: list[Any]):
    """Write a Python program to combine two lists into another list randomly."""
    output = one + two
    shuffle(output)
    return output


print(one_four_seven([1, 2, 7, 8, 3, 7], [4, 3, 8, 9, 4, 3, 8, 9]))


def one_four_eight(data: list[Any], remove: list[Any]):
    """Write a Python program to remove specific words from a given list."""
    return [word for word in data if word not in remove]


print(
    one_four_eight(
        ["red", "green", "blue", "white", "black", "orange"], ["white", "orange"]
    )
)
assert one_four_eight(
    ["red", "green", "blue", "white", "black", "orange"], ["white", "orange"]
) == ["red", "green", "blue", "black"]


def one_four_nine(data: set[Any]):
    """Write a Python program to get all possible combinations of the elements of a given list."""
    if not data:
        return set([()])

    expanded = [*data]
    output = []
    for other in one_four_nine(set(expanded[1:])):
        output.append(tuple(other))
        output.append(tuple(sorted([expanded[0], *other])))
    return set(output)


print(one_four_nine(set(["orange", "red", "green", "blue"])))
assert one_four_nine(set(["orange", "red", "green", "blue"])) == set(
    [
        (),
        ("blue",),
        ("green",),
        ("orange",),
        ("red",),
        ("blue", "green"),
        ("blue", "red"),
        ("blue", "orange"),
        ("green", "orange"),
        ("green", "red"),
        ("orange", "red"),
        ("blue", "green", "red"),
        ("blue", "green", "orange"),
        ("blue", "orange", "red"),
        ("green", "orange", "red"),
        ("blue", "green", "orange", "red"),
    ]
)
