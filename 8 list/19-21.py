from typing import Any


def nineteen(one: list[Any], two: list[Any]):
    """Write a Python program to calculate the difference between the two lists."""
    return [x for x in one if x not in two] + [x for x in two if x not in one]


print(nineteen([1, 3, 5, 7, 9], [1, 2, 4, 6, 7, 8]))
assert nineteen([1, 3, 5, 7, 9], [1, 2, 4, 6, 7, 8]) == [3, 5, 9, 2, 4, 6, 8]


def twenty(data: list[Any]):
    """Write a Python program access the index of a list."""
    return list(range(len(data)))


print(twenty([5, 15, 35, 8, 98]))
assert twenty([5, 15, 35, 8, 98]) == [0, 1, 2, 3, 4]


def twenty_one(data: list[str]):
    """Write a Python program to convert a list of characters into a string."""
    return "".join(data)


print(twenty_one(["a", "b", "c", "d"]))
assert twenty_one(["a", "b", "c", "d"]) == "abcd"
