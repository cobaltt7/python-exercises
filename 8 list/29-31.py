from typing import Any, Tuple, TypeVar


def twenty_nine(data: list[int]):
    """Write a Python program to get unique values from a list."""
    output = []
    for item in data:
        if item not in output:
            output.append(item)
    return output


print(twenty_nine([10, 20, 30, 40, 20, 50, 60, 40]))
assert twenty_nine([10, 20, 30, 40, 20, 50, 60, 40]) == [10, 20, 30, 40, 50, 60]


def thirty(data: list[Any]):
    """Write a Python program to find the second smallest number in a list."""
    output = {}
    for item in data:
        if item not in output:
            output[item] = 0
        output[item] += 1
    return output


print(thirty([10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]))
assert thirty([10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]) == {
    10: 4,
    20: 4,
    40: 2,
    50: 2,
    30: 1,
}

T = TypeVar("T", str, float)


def thirty_one(data: list[T], edges: Tuple[T, T]):
    """Write a Python program to count the number of elements in a list within a specified range."""
    return len([item for item in data if edges[0] <= item <= edges[1]])


print(thirty_one([10, 20, 30, 40, 40, 40, 70, 80, 99], (40, 100)))
assert thirty_one([10, 20, 30, 40, 40, 40, 70, 80, 99], (40, 100)) == 6
assert thirty_one(["a", "b", "c", "d", "e", "f"], ("a", "e")) == 5
