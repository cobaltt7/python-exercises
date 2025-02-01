from typing import Any


def thirty_eight(data: list[Any]):
    """
    Write a Python program to change the position of every n-th value to the (n+1)th in a list.
    """
    return [data[index - 1 if index % 2 else index + 1] for index in range(len(data))]


print(thirty_eight([0, 1, 2, 3, 4, 5]))
assert thirty_eight([0, 1, 2, 3, 4, 5]) == [1, 0, 3, 2, 5, 4]


def thirty_nine(data: list[int]):
    """Write a Python program to convert a list of multiple integers into a single integer."""
    return int("".join(map(str, data)))


print(thirty_nine([10, 20, 30, 40]))
assert thirty_nine([10, 20, 30, 40]) == 10203040
assert thirty_nine([11, 33, 50]) == 113350
