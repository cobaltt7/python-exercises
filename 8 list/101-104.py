from typing import Any


def one_zero_one(data: list[list[float]]):
    """
    Write a Python program to sort a given matrix in ascending order according to the sum of its
    rows.
    """
    return sorted(data, key=sum)


print(one_zero_one([[1, 2, 3], [2, 4, 5], [1, 1, 1]]))
assert one_zero_one([[1, 2, 3], [2, 4, 5], [1, 1, 1]]) == [
    [1, 1, 1],
    [1, 2, 3],
    [2, 4, 5],
]
assert one_zero_one([[1, 2, 3], [-2, 4, -5], [1, -1, 1]]) == [
    [-2, 4, -5],
    [1, -1, 1],
    [1, 2, 3],
]


def one_zero_two(data: list[str], size: int):
    """
    Write a Python program to extract specified size of strings from a give list of string values.
    """
    return [word for word in data if len(word) == size]


print(one_zero_two(["Python", "list", "exercises", "practice", "solution"], 8))
assert one_zero_two(["Python", "list", "exercises", "practice", "solution"], 8) == [
    "practice",
    "solution",
]


def one_zero_three(data: list[Any], count: int):
    """
    Write a Python program to extract specified number of elements from a given list, which follows
    each other continuously.
    """
    output = []
    current = None
    found = 0
    for item in data:
        if item == current:
            found += 1
        else:
            current = item
            found = 1
        if found == count:
            output.append(current)
            found = 0
    return output


print(one_zero_three([1, 1, 3, 4, 4, 5, 6, 7], 2))
assert one_zero_three([1, 1, 3, 4, 4, 5, 6, 7], 2) == [1, 4]
assert one_zero_three([0, 1, 2, 3, 4, 4, 4, 4, 5, 7], 4) == [4]


def one_zero_four(data: list[int]):
    """Write a Python program to find the difference between consecutive numbers in a given list."""
    return [item - data[index - 1] for index, item in list(enumerate(data))[1:]]


print(one_zero_four([1, 1, 3, 4, 4, 5, 6, 7]))
assert one_zero_four([1, 1, 3, 4, 4, 5, 6, 7]) == [0, 2, 1, 0, 1, 1, 1]
assert one_zero_four([4, 5, 8, 9, 6, 10]) == [1, 3, 1, -3, 4]
