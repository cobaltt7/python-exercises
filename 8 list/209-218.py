from typing import Any, Callable
from math import floor


def two_zero_nine(data: list[float]):
    """
    Write a Python program to count the number of groups of non-zero numbers separated by zeros in a
    given list of numbers.
    """
    count = 0
    in_group = False
    for item in data:
        if item == 0:
            in_group = False
        elif not in_group:
            count += 1
            in_group = True
    return count


print(
    two_zero_nine([
        3,
        4,
        6,
        2,
        0,
        0,
        0,
        0,
        0,
        0,
        6,
        7,
        6,
        9,
        10,
        0,
        0,
        0,
        0,
        0,
        5,
        9,
        9,
        7,
        4,
        4,
        0,
        0,
        0,
        0,
        0,
        0,
        5,
        3,
        2,
        9,
        7,
        1,
    ])
)
assert (
    two_zero_nine([
        3,
        4,
        6,
        2,
        0,
        0,
        0,
        0,
        0,
        0,
        6,
        7,
        6,
        9,
        10,
        0,
        0,
        0,
        0,
        0,
        5,
        9,
        9,
        7,
        4,
        4,
        0,
        0,
        0,
        0,
        0,
        0,
        5,
        3,
        2,
        9,
        7,
        1,
    ])
) == 4


def two_one_zero(data: list[float]):
    """
    Write a Python program to compute the sum of non-zero groups (separated by zeros) of a given
    list of numbers.
    """
    sums = []
    total = 0.0
    for item in data:
        if total != 0 and item == 0:
            sums.append(total)
            total = 0
        else:
            total += item
    return sums


print(
    two_one_zero([
        3,
        4,
        6,
        2,
        0,
        0,
        0,
        0,
        0,
        0,
        6,
        7,
        6,
        9,
        10,
        0,
        0,
        0,
        0,
        0,
        7,
        4,
        4,
        0,
        0,
        0,
        0,
        0,
        0,
        5,
        3,
        2,
        9,
        7,
        1,
        0,
        0,
        0,
    ])
)
assert (
    two_one_zero([
        3,
        4,
        6,
        2,
        0,
        0,
        0,
        0,
        0,
        0,
        6,
        7,
        6,
        9,
        10,
        0,
        0,
        0,
        0,
        0,
        7,
        4,
        4,
        0,
        0,
        0,
        0,
        0,
        0,
        5,
        3,
        2,
        9,
        7,
        1,
        0,
        0,
        0,
    ])
) == [15, 38, 15, 27]


def two_one_one(data: list[Any], index: int):
    """Write a Python program to remove an element from a given list."""
    return data[:index] + data[index + 1 :]


print(two_one_one(["Ricky Rivera", 98, "Math", 90, "Science"], 0))
assert (two_one_one(["Ricky Rivera", 98, "Math", 90, "Science"], 0)) == [
    98,
    "Math",
    90,
    "Science",
]


def two_one_two(data: list[Any]):
    """
    Write a Python program to remove all values except integer values from a given array of mixed
    values.
    """
    return [item for item in data if isinstance(item, int)]


print(two_one_two([34.67, 12, -94.89, "Python", 0, "C#"]))
assert (two_one_two([34.67, 12, -94.89, "Python", 0, "C#"])) == [12, 0]


def two_one_three(data: list[int]):
    """
    Write a Python program to calculate the sum of two lowest negative numbers in a given array of
    integers.

    An integer (from the Latin integer meaning "whole") is colloquially defined as a number that can
    be written without a fractional component. For example, 21, 4, 0, and -2048 are integers.
    """
    smallest = sorted(data)
    return smallest[0] + smallest[1]


print(two_one_three([-14, 15, -10, -11, -12, -13, 16, 17, 18, 19, 20]))
assert (two_one_three([-14, 15, -10, -11, -12, -13, 16, 17, 18, 19, 20])) == -27
assert (two_one_three([-4, 5, -2, 0, 3, -1, 4, 9])) == -6


def two_one_four(data: int):
    """
    Write a Python program to sort a given positive number in descending/ascending order.

    Descending -> Highest to lowest.

    Ascending -> Lowest to highest
    """
    digits = sorted(str(data))
    return (int("".join(digits[::-1])), int("".join(digits)))


print(two_one_four(134543))
assert (two_one_four(134543)) == (544331, 133445)
assert (two_one_four(43750973)) == (97754330, 3345779)


def two_one_five(data: list[list[Any]], fill: Any = None):
    """
    Write a Python program to merge two or more lists into a list of lists, combining elements from
    each of the input lists based on their positions.
    """
    length = len(sorted(data, key=len, reverse=True)[0])
    output: list[list[Any]] = []
    for i in range(length):
        output.append([])
        for sublist in data:
            output[-1].append(sublist[i] if len(sublist) > i else fill)
    return output


print(two_one_five([["a", "b"], [1, 2], [True, False]]))
assert (two_one_five([["a", "b"], [1, 2], [True, False]])) == [
    ["a", 1, True],
    ["b", 2, False],
]
assert (two_one_five([["a"], [1, 2], [True, False]])) == [
    ["a", 1, True],
    [None, 2, False],
]
assert (two_one_five([["a"], [1, 2], [True, False]], "_")) == [
    ["a", 1, True],
    ["_", 2, False],
]


def two_one_six(data: list[Any], function: Callable):
    """
    Write a  Python program to group the elements of a list based on the given function and return
    the count of elements in each group.
    """
    output: dict[Any, int] = {}
    for item in data:
        result = function(item)
        if result in output:
            output[result] += 1
        else:
            output[result] = 1
    return output


print(two_one_six([6.1, 4.2, 6.3], floor))
assert two_one_six([6.1, 4.2, 6.3], floor) == {6: 2, 4: 1}
assert two_one_six(["one", "two", "three"], len) == {3: 2, 5: 1}


def two_one_seven(data: list[Any], function: Callable):
    """
    Write a Python program to split values into two groups, based on the result of the given
    filtering function.
    """
    output: list[list[Any]] = [[], []]
    for item in data:
        result = function(item)
        output[0 if result else 1].append(item)
    return output


print(two_one_seven(["red", "green", "black", "white"], lambda x: x[0] == "w"))
assert two_one_seven(["red", "green", "black", "white"], lambda x: x[0] == "w") == [
    ["white"],
    ["red", "green", "black"],
]


def two_one_eight(data: list[Any], indicies: list[int], reverse=False):
    """
    Write a Python program to sort one list based on another list containing the desired indexes.
    """
    return sorted(data, key=lambda item: indicies[data.index(item)], reverse=reverse)


print(
    two_one_eight(
        ["eggs", "bread", "oranges", "jam", "apples", "milk"], [3, 2, 6, 4, 1, 5]
    )
)
assert (
    two_one_eight(
        ["eggs", "bread", "oranges", "jam", "apples", "milk"], [3, 2, 6, 4, 1, 5]
    )
) == ["apples", "bread", "eggs", "jam", "milk", "oranges"]
assert (
    two_one_eight(
        ["eggs", "bread", "oranges", "jam", "apples", "milk"], [3, 2, 6, 4, 1, 5], True
    )
) == ["oranges", "milk", "jam", "eggs", "bread", "apples"]
