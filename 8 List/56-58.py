from ast import literal_eval
from typing import Any


def five_six(literal: str):
    """Write a Python program to convert a string to a list."""
    return literal_eval(literal)


print(five_six("['Red', 'Green', 'White']"))
assert five_six("['Red', 'Green', 'White']") == ["Red", "Green", "White"]


def five_seven(data: list[str], string: str):
    """
    Write a Python program to check if all items in a given list of strings are equal to a given
    string.
    """
    return all(map(lambda item: item == string, data))


print(five_seven(["green", "orange", "black", "white"], "blue"))
assert five_seven(["green", "orange", "black", "white"], "blue") is False
assert five_seven(["green", "green", "green", "green"], "green") is True


def five_eight(one: list[Any], two: list[Any]):
    """Write a Python program to replace the last element in a list with another list."""
    return one[:-1] + two


print(five_eight([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]))
assert five_eight([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 2, 4, 6, 8]
