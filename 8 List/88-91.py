from typing import Any


def eight_eight(data: str):
    """
    Write a Python program to read a square matrix from the console and print the sum of the
    matrix's primary diagonal. Accept the size of the square matrix and elements for each column
    separated with a space (for every row) as input from the user.
    """
    matrix = [[float(item) for item in row.split(" ")] for row in data.split("\n")]
    return sum(row[index] for index, row in enumerate(matrix))


print(eight_eight("2 3 4\n4 5 6\n3 4 7"))
assert eight_eight("2 3 4\n4 5 6\n3 4 7") == 14


def eight_nine(one: list[list[Any]], two: list[list[Any]]):
    """Write a Python program to Zip two given lists of lists."""
    return [sublist + two[index] for index, sublist in enumerate(one)]


print(eight_nine([[1, 3], [5, 7], [9, 11]], [[2, 4], [6, 8], [10, 12, 14]]))
assert eight_nine([[1, 3], [5, 7], [9, 11]], [[2, 4], [6, 8], [10, 12, 14]]) == [
    [1, 3, 2, 4],
    [5, 7, 6, 8],
    [9, 11, 10, 12, 14],
]


def nine_zero(data: list[Any]):
    """Write a Python program to count the number of lists in a given list of lists."""
    return len([item for item in data if isinstance(item, list)])


print(nine_zero([[1, 3], [5, 7], [9, 11], [13, 15, 17]]))
assert nine_zero([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4
assert nine_zero([[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]) == 3
assert nine_zero([4, [[6, 8], [4, 5, 8]], [10, 12, 14]]) == 2


def nine_one(data: list[list[Any]]):
    """Write a Python program to find a list with maximum and minimum lengths."""
    return sorted(data, key=len)[-1 :: -1 * (len(data) - 1)]


print(nine_one([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))
assert nine_one([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]) == [[13, 15, 17], [0]]
assert nine_one([[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]) == [[3, 5, 7], [0]]
assert nine_one([[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]) == [
    [1, 34, 5, 7],
    [12],
]
