from typing import Any


def one_two_zero(data: list[Any]):
    """Write a Python program to create a list taking alternate elements from a given list."""
    return [item for index, item in enumerate(data) if index % 2 == 0]


print(one_two_zero(["red", "black", "white", "green", "orange"]))
assert one_two_zero(["red", "black", "white", "green", "orange"]) == [
    "red",
    "white",
    "orange",
]
assert one_two_zero([2, 0, 3, 4, 0, 2, 8, 3, 4, 2]) == [2, 3, 0, 8, 4]


def one_two_one(search: list[Any], data: list[list[Any]]):
    """Write a Python program to find nested list elements that are present in another list."""
    return [[item for item in sublist if item in search] for sublist in data]


print(
    one_two_one(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]],
    )
)
assert one_two_one(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]],
) == [[12], [7, 11], [1, 5, 8]]


def one_two_two(data: list[Any]):
    """Write a Python program to find common element(s) in a given nested lists."""
    return set(item for item in data[0] if all(item in sublist for sublist in data[1:]))


print(
    one_two_two([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]])
)
assert one_two_two(
    [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
) == {18, 12}
