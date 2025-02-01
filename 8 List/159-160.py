from typing import Any


def one_five_nine(initial: list[Any], value: Any, times=1):
    """
    Write a Python program to append the same value /a list multiple times to a list/list-of-lists.
    """
    return initial + times * [value]


print(one_five_nine([], "7", 5))
assert one_five_nine([], "7", 5) == ["7", "7", "7", "7", "7"]
assert one_five_nine([1, 2, 3, 4], 5, 6) == [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]
assert one_five_nine([], [1, 2, 5], 4) == [[1, 2, 5], [1, 2, 5], [1, 2, 5], [1, 2, 5]]
assert one_five_nine([[5, 6, 7]], [1, 2, 5], 4) == [
    [5, 6, 7],
    [1, 2, 5],
    [1, 2, 5],
    [1, 2, 5],
    [1, 2, 5],
]


def one_six_zero(data: list[Any], count: int, condition):
    """
    Write a Python program to remove first specified number of elements from a given list
    satisfying a condition.
    """
    output = []
    removed = 0
    for item in data:
        if removed == count:
            output.append(item)
        elif condition(item):
            removed += 1
        else:
            output.append(item)
    return output


print(
    one_six_zero(
        [3, 10, 4, 7, 5, 7, 8, 3, 3, 4, 5, 9, 3, 4, 9, 8, 5],
        4,
        lambda item: item % 2 == 0,
    )
)
assert one_six_zero(
    [3, 10, 4, 7, 5, 7, 8, 3, 3, 4, 5, 9, 3, 4, 9, 8, 5], 4, lambda item: item % 2 == 0
) == [3, 7, 5, 7, 3, 3, 5, 9, 3, 4, 9, 8, 5]
