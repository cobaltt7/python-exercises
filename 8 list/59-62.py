from typing import Any


def five_nine(data: list[Any]):
    """Write a Python program to check if the n-th element exists in a given list."""
    return data[-1]


print(five_nine([1, 2, 3, 4, 5, 6]))
assert five_nine([1, 2, 3, 4, 5, 6]) == 6


def six_zero(data: list[tuple[float, float]]):
    """
    Write a Python program to find a tuple, the smallest second index value from a list of tuples.
    """
    return min(data, key=lambda item: item[1])


print(six_zero([(4, 1), (1, 2), (6, 0)]))
assert six_zero([(4, 1), (1, 2), (6, 0)]) == (6, 0)


def six_one(count: int = 2):
    """Write a Python program to create a list of empty dictionaries."""
    return [{} for _ in range(count)]


print(six_one())
assert six_one() == [{}, {}]
assert six_one(5) == [{}, {}, {}, {}, {}]


def six_two(data: list[int]):
    """Write a Python program to print a list of space-separated elements."""
    return " ".join(map(str, data))


print(six_two([1, 2, 3, 4, 5]))
assert six_two([1, 2, 3, 4, 5]) == "1 2 3 4 5"
