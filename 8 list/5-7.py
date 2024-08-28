from typing import Any


def five(data: list[Any]):
    """
    Write a Python program to count the number of strings from a given list of strings. The string
    length is 2 or more and the first and last characters are the same.
    """
    return len(
        [
            entry
            for entry in data
            if isinstance(entry, str) and len(entry) > 2 and entry[0] == entry[-1]
        ]
    )


print(five(["abc", "xyz", "aba", "1221"]))
assert five(["abc", "xyz", "aba", "1221"]) == 2
assert five(["ab", "xyzx", "aa", 1221]) == 1


def six(data: list[tuple[float, float]]):
    """
    Write a Python program to get a list, sorted in increasing order by the last element in each
    tuple from a given list of non-empty tuples.
    """
    return sorted(data, key=lambda item: item[-1])


print(six([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
assert six([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]) == [
    (2, 1),
    (1, 2),
    (2, 3),
    (4, 4),
    (2, 5),
]


def seven(data: list[Any]):
    """Write a Python program to remove duplicates from a list."""
    return [item for index, item in enumerate(data) if data.index(item) == index]


print(seven([10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]))
assert seven([10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]) == [
    10,
    20,
    30,
    50,
    60,
    40,
    80,
]
