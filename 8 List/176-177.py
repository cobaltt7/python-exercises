from typing import Any


def one_seven_six(one: list[float], two: list[float]):
    """Write a Python program to create a new list by dividing two given lists of numbers."""
    return [x / y for x, y in zip(one, two)]


print(one_seven_six([7, 2, 3, 4, 9, 2, 3], [9, 8, 2, 3, 3, 1, 2]))
assert one_seven_six([7, 2, 3, 4, 9, 2, 3], [9, 8, 2, 3, 3, 1, 2]) == [
    0.7777777777777778,
    0.25,
    1.5,
    1.3333333333333333,
    3.0,
    2.0,
    1.5,
]


def one_seven_seven(data: list[list[Any]]):
    """Write a Python program to find common elements in a given list of lists."""
    return set(item for item in data[0] if all(item in sublist for sublist in data[1:]))


print(one_seven_seven([[7, 2, 3, 4, 7], [9, 2, 3, 2, 5], [8, 2, 3, 4, 4]]))
assert one_seven_seven([[7, 2, 3, 4, 7], [9, 2, 3, 2, 5], [8, 2, 3, 4, 4]]) == {2, 3}
assert one_seven_seven([["a", "b", "c"], ["b", "c", "d"], ["c", "d", "e"]]) == {"c"}
