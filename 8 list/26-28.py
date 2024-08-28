from typing import Any


def twenty_six(one: list[int], two: list[int]):
    """Write a Python program to check whether two lists are circularly identical."""
    return " ".join(map(str, sorted(one))) == " ".join(map(str, sorted(two)))


list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]

print(twenty_six([10, 10, 0, 0, 10], [10, 10, 10, 0, 0]))
assert twenty_six([10, 10, 0, 0, 10], [10, 10, 10, 0, 0]) is True
assert twenty_six([10, 10, 0, 0, 10], [1, 10, 10, 0, 0]) is False


def twenty_seven(data: list[Any]):
    """Write a Python program to find the second smallest number in a list."""
    items = sorted(set(data))
    return items[1] if len(items) > 1 else None


print(twenty_seven([1, 2, 3]))
assert twenty_seven([1, 2, 3]) == 2
assert twenty_seven([1, 2, -8, -2, 0, -2]) == -2
assert twenty_seven([1, 1, 0, 0, 2, -2, -2]) == 0
assert twenty_seven([1, 1, 1, 0, 0, 0, 2, -2, -2]) == 0
assert twenty_seven([2, 2]) is None
assert twenty_seven([2]) is None


def twenty_eight(data: list[Any]):
    """Write a Python program to find the second smallest number in a list."""
    items = sorted(set(data))
    return items[-2] if len(items) > 1 else None


print(twenty_eight([1, 2, 3, 4, 4]))
assert twenty_eight([1, 2, 3, 4, 4]) == 3
assert twenty_eight([1, 1, 1, 0, 0, 0, 2, -2, -2]) == 1
assert twenty_eight([2, 2]) is None
assert twenty_eight([1]) is None
