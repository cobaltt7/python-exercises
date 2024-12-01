from collections.abc import Iterable, Sequence
from typing import Any


def one_eight_six(data: list[Any], indexes: tuple[tuple[int, int], tuple[int, int]]):
    """Write a Python program to swap two sublists in a given list."""
    output = [*data]
    output[indexes[0][0] : indexes[0][1]], output[indexes[1][0] : indexes[1][1]] = (
        output[indexes[1][0] : indexes[1][1]],
        output[indexes[0][0] : indexes[0][1]],
    )
    return output


print(
    one_eight_six(
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], ((1, 3), (4, 6))
    )
)
assert one_eight_six(
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], ((6, 10), (1, 3))
) == [0, 6, 7, 8, 9, 3, 4, 5, 1, 2, 10, 11, 12, 13, 14, 15]
assert one_eight_six(
    [0, 6, 7, 8, 9, 3, 4, 5, 1, 2, 10, 11, 12, 13, 14, 15], ((1, 3), (4, 6))
) == [0, 9, 3, 8, 6, 7, 4, 5, 1, 2, 10, 11, 12, 13, 14, 15]


def one_eight_seven(data: list[Iterable[str]]):
    """Write a Python program to convert a given list of tuples to a list of strings."""
    return [" ".join(words) for words in data]


print(one_eight_seven([("red", "green"), ("black", "white"), ("orange", "pink")]))
assert one_eight_seven([("red", "green"), ("black", "white"), ("orange", "pink")]) == [
    "red green",
    "black white",
    "orange pink",
]
assert one_eight_seven(
    [
        ("Laiba", "Delacruz"),
        ("Mali", "Stacey", "Drummond"),
        ("Raja", "Welch"),
        ("Saarah", "Stone"),
    ]
) == ["Laiba Delacruz", "Mali Stacey Drummond", "Raja Welch", "Saarah Stone"]


def one_eight_eight(data: list[Sequence[Any]], index: int):
    """Write a Python program to sort a given list of tuples on specified element."""
    return sorted(data, key=lambda item: item[index - 1])


print(
    one_eight_eight(
        [
            ("item2", 10, 10.12),
            ("item3", 15, 25.1),
            ("item1", 11, 24.5),
            ("item4", 12, 22.5),
        ],
        1,
    )
)
assert one_eight_eight(
    [
        ("item2", 10, 10.12),
        ("item3", 15, 25.1),
        ("item1", 11, 24.5),
        ("item4", 12, 22.5),
    ],
    1,
) == [
    ("item1", 11, 24.5),
    ("item2", 10, 10.12),
    ("item3", 15, 25.1),
    ("item4", 12, 22.5),
]
assert one_eight_eight(
    [
        ("item2", 10, 10.12),
        ("item3", 15, 25.1),
        ("item1", 11, 24.5),
        ("item4", 12, 22.5),
    ],
    2,
) == [
    ("item2", 10, 10.12),
    ("item1", 11, 24.5),
    ("item4", 12, 22.5),
    ("item3", 15, 25.1),
]
assert one_eight_eight(
    [
        ("item2", 10, 10.12),
        ("item3", 15, 25.1),
        ("item1", 11, 24.5),
        ("item4", 12, 22.5),
    ],
    3,
) == [
    ("item2", 10, 10.12),
    ("item4", 12, 22.5),
    ("item1", 11, 24.5),
    ("item3", 15, 25.1),
]
