from typing import Any


def six_three(data: list[str | float], string: str):
    """Write a Python program to insert a given string at the beginning of all items in a list."""
    return [string + str(item) for item in data]


print(six_three([1, 2, 3, 4], "emp"))
assert six_three([1, 2, 3, 4], "emp") == ["emp1", "emp2", "emp3", "emp4"]


def six_four(one: list[Any], two: list[Any]):
    """Write a Python program to iterate over two lists simultaneously."""
    return list(zip(one, two))


print(six_four([1, 2, 3], ["red", "white", "black"]))
assert six_four([1, 2, 3], ["red", "white", "black"]) == [
    (1, "red"),
    (2, "white"),
    (3, "black"),
]


def six_five(data: list[float]):
    """Write a Python program to move all zero digits to end of a given list of numbers."""
    return sorted(data, key=lambda item: item == 0)


print(
    six_five(
        [
            3,
            4,
            0,
            0,
            0,
            6,
            2,
            0,
            6,
            7,
            6,
            0,
            0,
            0,
            9,
            10,
            7,
            4,
            4,
            5,
            3,
            0,
            0,
            2,
            9,
            7,
            1,
        ]
    )
)
assert six_five(
    [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
) == [3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def six_six(data: list[list[float]]):
    """
    Write a Python program to find the list in a list of lists whose sum of elements is the highest.
    """
    return sorted(data, key=sum)[-1]


print(six_six([[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]))
assert six_six([[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]) == [10, 11, 12]
