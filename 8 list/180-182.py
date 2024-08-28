from typing import Any


def one_eight_zero(data: list[int]):
    """
    Write a Python program to create the smallest possible number using the elements of a given list
    of positive integers.
    """
    numbers = sorted(
        (str(number) for number in data),
        key=lambda number: int(number) / (10 ** (len(number) - 1)),
    )
    return int("".join(numbers))


print(one_eight_zero([3, 40, 41, 43, 74, 9]))
assert one_eight_zero([3, 40, 41, 43, 74, 9]) == 3404143749
assert one_eight_zero([10, 40, 20, 30, 50, 60]) == 102030405060
assert one_eight_zero([910, 40, 120, 30, 504, 60]) == 120304050460910
assert one_eight_zero([8, 4, 2, 9, 5, 6, 1, 0]) == 1245689


def one_eight_one(data: list[Any], index: int):
    """Write a Python program to iterate a given list cyclically on specific index position."""
    return data[index:] + data[:index]


print(one_eight_one(["a", "b", "c", "d", "e", "f", "g", "h"], 3))
assert one_eight_one(["a", "b", "c", "d", "e", "f", "g", "h"], 3) == [
    "d",
    "e",
    "f",
    "g",
    "h",
    "a",
    "b",
    "c",
]
assert one_eight_one(["a", "b", "c", "d", "e", "f", "g", "h"], 5) == [
    "f",
    "g",
    "h",
    "a",
    "b",
    "c",
    "d",
    "e",
]


def one_eight_two(data: list[list[float]]):
    """
    Write a Python program to calculate the maximum and minimum sum of a sublist in a given list of
    lists.
    """
    sorted_lists = sorted(data, key=sum)
    return (sorted_lists[-1], sorted_lists[0])


print(
    one_eight_two(
        [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
    )
)
assert one_eight_two(
    [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
) == ([2, 3, 5, 4], [1, 2, 1, 2])
