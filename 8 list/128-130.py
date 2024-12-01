from typing import Any


def one_two_eight(data: list[float], indices: tuple[int, int]):
    """
    Write a Python program to calculate the sum of the numbers in a list between the indices of a
    specified range.
    """
    return sum(data[indices[0] : indices[1] + 1])


print(one_two_eight([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], (8, 10)))
assert one_two_eight([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], (8, 10)) == 29


def one_two_nine(data: list[list[Any]]):
    """Write a Python program to reverse each list in a given list of lists."""
    return [sublist[::-1] for sublist in data]


print(one_two_nine([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
assert one_two_nine(
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
) == [[4, 3, 2, 1], [8, 7, 6, 5], [12, 11, 10, 9], [16, 15, 14, 13]]


def one_three_zero(data: list[list[Any]]):
    """Write a Python program to count the same pair in three given lists."""
    return len(
        [
            item
            for index, item in enumerate(data[0])
            if all(item == sublist[index] for sublist in data[1:])
        ]
    )


print(
    one_three_zero(
        [[1, 2, 3, 4, 5, 6, 7, 8], [2, 2, 3, 1, 2, 6, 7, 9], [2, 1, 3, 1, 2, 6, 7, 9]]
    )
)
assert (
    one_three_zero(
        [[1, 2, 3, 4, 5, 6, 7, 8], [2, 2, 3, 1, 2, 6, 7, 9], [2, 1, 3, 1, 2, 6, 7, 9]]
    )
    == 3
)
