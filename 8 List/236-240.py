from typing import Any, Union, Callable


def two_three_six(data: list[Any]):
    """Write a Python program to find the items that are parity outliers in a given list."""
    even = []
    odd = []
    for item in data:
        if item % 2 == 0:
            even.append(item)
        else:
            odd.append(item)
    return odd if len(even) > len(odd) else even


print(two_three_six([1, 2, 3, 4, 6]))
assert two_three_six([1, 2, 3, 4, 6]) == [1, 3]
assert two_three_six([1, 2, 3, 4, 5, 6, 7]) == [2, 4, 6]


def two_three_seven(data: list[Any], key: Union[str, int]):
    """
    Write a Python program to convert a given list of dictionaries into a list of values
    corresponding to the specified key.
    """
    return [item[key] for item in data]


print(
    two_three_seven(
        [
            {"name": "Areeba", "age": 8},
            {"name": "Zachariah", "age": 36},
            {"name": "Caspar", "age": 34},
            {"name": "Presley", "age": 10},
        ],
        "age",
    )
)
assert two_three_seven(
    [
        {"name": "Areeba", "age": 8},
        {"name": "Zachariah", "age": 36},
        {"name": "Caspar", "age": 34},
        {"name": "Presley", "age": 10},
    ],
    "age",
) == [8, 36, 34, 10]


def two_three_eight(data: list[Any], callback: Callable):
    """
    Write a Python program to calculate the average of a given list, after mapping each element to a
    value using the provided function.
    """
    return sum(callback(item) for item in data) / len(data)


print(two_three_eight([{"n": 4}, {"n": 2}, {"n": 8}, {"n": 6}], lambda x: x["n"]))
assert (
    two_three_eight([{"n": 4}, {"n": 2}, {"n": 8}, {"n": 6}], lambda x: x["n"])
) == 5.0
assert (
    two_three_eight([{"n": 10}, {"n": 20}, {"n": -30}, {"n": 60}], lambda x: x["n"])
) == 15.0


def two_three_nine(data: list[Any], callback: Callable):
    """
    Write a Python program to find the value of the first element in the given list that satisfies
    the provided testing function.
    """
    return next(filter(callback, data))


print(two_three_nine([1, 2, 3, 4], lambda n: n % 2 == 1))
assert (two_three_nine([1, 2, 3, 4], lambda n: n % 2 == 1)) == 1
assert (two_three_nine([1, 2, 3, 4], lambda n: n % 2 == 0)) == 2


def two_four_zero(data: list[Any], callback: Callable):
    """
    Write a Python program to find the value of the last element in the given list that satisfies
    the provided testing function.
    """
    return next(filter(callback, data[::-1]))


print(two_four_zero([1, 2, 3, 4], lambda n: n % 2 == 1))
assert (two_four_zero([1, 2, 3, 4], lambda n: n % 2 == 1)) == 53
assert (two_four_zero([1, 2, 3, 4], lambda n: n % 2 == 0)) == 4
