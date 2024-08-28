from typing import Any


def one_zero_five(one: list[float], two: list[float]):
    """Write a Python program to compute average of two given lists."""
    numbers = one + two
    return sum(numbers) / len(numbers)


print(one_zero_five([1, 1, 3, 4, 4, 5, 6, 7], [0, 1, 2, 3, 4, 4, 5, 7, 8]))
assert (
    one_zero_five([1, 1, 3, 4, 4, 5, 6, 7], [0, 1, 2, 3, 4, 4, 5, 7, 8])
    == 3.823529411764706
)


def one_zero_six(data: list[Any]):
    """Write a Python program to count integers in a given mixed list."""
    return len([item for item in data if isinstance(item, int)])


print(one_zero_six([1, "abcd", 3, 1.2, 4, "xyz", 5, "pqr", 7, -5, -12.22]))
assert one_zero_six([1, "abcd", 3, 1.2, 4, "xyz", 5, "pqr", 7, -5, -12.22]) == 6


def one_zero_seven(data: list[Any], column: int):
    """Write a Python program to remove a specified column from a given nested list."""
    return [sublist[: column - 1] + sublist[column:] for sublist in data]


print(one_zero_seven([[1, 2, 3], [2, 4, 5], [1, 1, 1]], 1))
assert one_zero_seven([[1, 2, 3], [2, 4, 5], [1, 1, 1]], 1) == [[2, 3], [4, 5], [1, 1]]
assert one_zero_seven([[1, 2, 3], [-2, 4, -5], [1, -1, 1]], 3) == [
    [1, 2],
    [-2, 4],
    [1, -1],
]
