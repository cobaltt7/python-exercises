from typing import Any


def two_six_six(value: Any):
    """Write a Python program to cast the provided value as a list if it's not one."""
    return list(value)


print(two_six_six([1]))
assert two_six_six([1]) == [1]
assert two_six_six(("Red", "Green")) == ["Red", "Green"]
assert two_six_six({"Red", "Green"}) in [["Green", "Red"], ["Red", "Green"]]
assert two_six_six({1: "Red", 2: "Green", 3: "Black"}) == [1, 2, 3]


def two_six_seven(data: list[float]):
    """
    Write a Python program to get the cumulative sum of the elements of a given list.
    """
    current: float = 0
    output = []
    for item in data:
        current += item
        output.append(current)
    return output


print(two_six_seven([1, 2, 3, 4]))
assert two_six_seven([1, 2, 3, 4]) == [1, 3, 6, 10]
assert two_six_seven([-1, -2, -3, 4]) == [-1, -3, -6, -2]


def two_six_eight(data: list[Any], count: int):
    """
    Write a Python program to get a list with n elements removed from the left and
    right.
    """
    count -= len(data)
    return [data[count:], data[:-count]]


print(two_six_eight([1, 2, 3, 4, 5, 6], 7))
assert two_six_eight([1, 2, 3], 1) == [[2, 3], [1, 2]]
assert two_six_eight([1, 2, 3, 4], 2) == [[3, 4], [1, 2]]
assert two_six_eight([1, 2, 3, 4, 5, 6], 7) == [[2, 3, 4, 5, 6], [1, 2, 3, 4, 5]]


def two_six_nine(data: list[Any], interval: int):
    """Write a Python program to get every nth element in a given list."""
    return data[interval - 1 :: interval]


print(two_six_nine([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
assert two_six_nine([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) == [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
]
assert two_six_nine([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2) == [2, 4, 6, 8, 10]
assert two_six_nine([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == [5, 10]
assert two_six_nine([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6) == [6]


def two_seven_zero(one: list[Any], two: list[Any]):
    """
    Write a Python program to check if the elements of the first list are contained in
    the second one regardless of order.
    """
    search_array = [*two]
    for item in one:
        if item in search_array:
            search_array.remove(item)
        else:
            return False
    return True


print(two_seven_zero([1, 2], [2, 4, 1]))
assert two_seven_zero([1, 2], [2, 4, 1]) is True
assert two_seven_zero([1], [2, 4, 1]) is True
assert two_seven_zero([1, 1], [4, 2, 1]) is False
assert two_seven_zero([1, 1], [3, 2, 4, 1, 5, 1]) is True
