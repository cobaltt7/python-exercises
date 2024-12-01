from functools import reduce
from typing import Any


def one_two_six(data: list[list[Any]]):
    """Write a Python program to interleave multiple lists of the same length."""
    return [
        item
        for index in range(len(data[0]))
        for item in [sublist[index] for sublist in data]
    ]


print(
    one_two_six([
        [1, 2, 3, 4, 5, 6, 7],
        [10, 20, 30, 40, 50, 60, 70],
        [100, 200, 300, 400, 500, 600, 700],
    ])
)
assert one_two_six([
    [1, 2, 3, 4, 5, 6, 7],
    [10, 20, 30, 40, 50, 60, 70],
    [100, 200, 300, 400, 500, 600, 700],
]) == [
    1,
    10,
    100,
    2,
    20,
    200,
    3,
    30,
    300,
    4,
    40,
    400,
    5,
    50,
    500,
    6,
    60,
    600,
    7,
    70,
    700,
]


def one_two_seven(data: list[str], splitters: list[str]):
    """
    Write a Python program to remove words from a given list of strings containing a character or
    string.
    """
    return set(
        x
        for word in data
        for x in reduce(
            lambda words, splitter: [
                parts for word in words for parts in word.split(splitter)
            ],
            splitters + [" "],
            [word],
        )
    )


print(
    one_two_seven(
        ["Red color", "Orange#", "Green", "Orange @", "White"], ["#", "color", "@"]
    )
)
assert one_two_seven(
    ["Red color", "Orange#", "Green", "Orange @", "White"], ["#", "color", "@"]
) == {"", "White", "Red", "Green", "Orange"}
