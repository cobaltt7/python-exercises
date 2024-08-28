from typing import Any, Sequence


def one_one_four(data: list[tuple[Any, ...]], index: int):
    """Write a Python program to extract the nth element from a given list of tuples."""
    return [sublist[index] for sublist in data]


print(
    one_one_four(
        [
            ("Greyson Fulton", 98, 99),
            ("Brady Kent", 97, 96),
            ("Wyatt Knott", 91, 94),
            ("Beau Turnbull", 94, 98),
        ],
        0,
    )
)
assert one_one_four(
    [
        ("Greyson Fulton", 98, 99),
        ("Brady Kent", 97, 96),
        ("Wyatt Knott", 91, 94),
        ("Beau Turnbull", 94, 98),
    ],
    0,
) == ["Greyson Fulton", "Brady Kent", "Wyatt Knott", "Beau Turnbull"]
assert one_one_four(
    [
        ("Greyson Fulton", 98, 99),
        ("Brady Kent", 97, 96),
        ("Wyatt Knott", 91, 94),
        ("Beau Turnbull", 94, 98),
    ],
    2,
) == [99, 96, 94, 98]


def one_one_five(data: list[Any]):
    """Write a Python program to check if the elements of a given list are unique or not."""
    return len(set(data)) == len(data)


print(one_one_five([1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]))
assert one_one_five([1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]) is False
assert one_one_five([2, 4, 6, 8, 10, 12, 14]) is True


def one_one_six(data: list[Sequence[Any]], index: int):
    """Write a Python program to sort a list of lists by a given index of the inner list."""
    return sorted(data, key=lambda item: item[index])


print(
    one_one_six(
        [
            ("Greyson Fulton", 98, 99),
            ("Brady Kent", 97, 96),
            ("Wyatt Knott", 91, 94),
            ("Beau Turnbull", 94, 98),
        ],
        0,
    )
)
assert one_one_six(
    [
        ("Greyson Fulton", 98, 99),
        ("Brady Kent", 97, 96),
        ("Wyatt Knott", 91, 94),
        ("Beau Turnbull", 94, 98),
    ],
    0,
) == [
    ("Beau Turnbull", 94, 98),
    ("Brady Kent", 97, 96),
    ("Greyson Fulton", 98, 99),
    ("Wyatt Knott", 91, 94),
]
assert one_one_six(
    [
        ("Greyson Fulton", 98, 99),
        ("Brady Kent", 97, 96),
        ("Wyatt Knott", 91, 94),
        ("Beau Turnbull", 94, 98),
    ],
    2,
) == [
    ("Wyatt Knott", 91, 94),
    ("Brady Kent", 97, 96),
    ("Beau Turnbull", 94, 98),
    ("Greyson Fulton", 98, 99),
]
