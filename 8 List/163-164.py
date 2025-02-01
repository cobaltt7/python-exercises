from typing import Any


def one_six_three(data: list[Any], search: Any):
    """
    Write a Python program to check if a given list increases strictly. Moreover, if removing only
    one element from the list results in a strictly increasing list, we still consider the list
    true.
    """
    return next(index for index, item in enumerate(data) if item > search)


print(one_six_three([12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83], 73))
assert one_six_three([12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83], 73) == 4
assert one_six_three([12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83], 21) == 1
assert one_six_three([12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83], 80) == 5
assert one_six_three([12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83], 55) == 3


def one_six_four(data: list[Any], search: Any):
    """Write a Python program to get the items from a given list with specific condition."""
    return sum(1 for item in data if item > search and item % 2 == 0)


print(one_six_four([12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83], 45))
assert (
    one_six_four([12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83], 45) == 5
)
