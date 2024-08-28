from typing import Any


def one_four_two(data: list[list[float]], index: int):
    """Write a Python program to sum a specific column of a list in a given list of lists."""
    return sum(sublist[index - 1] for sublist in data)


print(one_four_two([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]], 1))
assert one_four_two([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]], 1) == 12
assert one_four_two([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]], 2) == 15
assert one_four_two([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]], 4) == 9


def one_four_three(data: list[list[Any]]):
    """Write a Python program to get the frequency of the elements in a given list of lists."""
    output = {}
    for sublist in data:
        for item in sublist:
            if item not in output:
                output[item] = 0
            output[item] += 1
    return output


print(one_four_three([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]))
assert one_four_three([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]) == {
    1: 1,
    2: 3,
    3: 1,
    4: 1,
    5: 2,
    6: 1,
    7: 1,
    8: 1,
    9: 1,
}


def one_four_four(data: list[list[Any]], index: int):
    """
    Write a Python program to extract every first or specified element from a given two-dimensional
    list.
    """
    return [sublist[index - 1] for sublist in data]


print(one_four_four([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]], 1))
assert one_four_four([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]], 1) == [1, 4, 7]
assert one_four_four([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]], 3) == [3, 6, 9]
