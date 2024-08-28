from typing import Any


def one_five_three(data: list[Any], search: Any, threshold: int):
    """Write a Python program to check if a given element occurs at least n times in a list."""
    return sum(1 for item in data if item == search) >= threshold


print(one_five_three([0, 1, 3, 5, 0, 3, 4, 5, 0, 8, 0, 3, 6, 0, 3, 1, 1, 0], 3, 4))
assert (
    one_five_three([0, 1, 3, 5, 0, 3, 4, 5, 0, 8, 0, 3, 6, 0, 3, 1, 1, 0], 3, 4) is True
)
assert (
    one_five_three([0, 1, 3, 5, 0, 3, 4, 5, 0, 8, 0, 3, 6, 0, 3, 1, 1, 0], 0, 5) is True
)
assert (
    one_five_three([0, 1, 3, 5, 0, 3, 4, 5, 0, 8, 0, 3, 6, 0, 3, 1, 1, 0], 8, 3) is False
)


def one_five_four(one: list[list[Any]], two: list[list[Any]]):
    """Write a Python program to join two given list of lists of same length, element wise."""
    return [item + two[index] for index, item in enumerate(one)]


print(
    one_five_four(
        [[10, 20], [30, 40], [50, 60], [30, 20, 80]],
        [[61], [12, 14, 15], [12, 13, 19, 20], [12]],
    )
)
assert one_five_four(
    [[10, 20], [30, 40], [50, 60], [30, 20, 80]],
    [[61], [12, 14, 15], [12, 13, 19, 20], [12]],
) == [[10, 20, 61], [30, 40, 12, 14, 15], [50, 60, 12, 13, 19, 20], [30, 20, 80, 12]]
assert one_five_four(
    [["a", "b"], ["b", "c", "d"], ["e", "f"]],
    [["p", "q"], ["p", "s", "t"], ["u", "v", "w"]],
) == [["a", "b", "p", "q"], ["b", "c", "d", "p", "s", "t"], ["e", "f", "u", "v", "w"]]
