from typing import Any, Callable, Iterable, List, Sized


def two_four_one(data: List[Any]):
    """
    Write a Python program to create a dictionary with the unique values of a given list as keys and
    their frequencies as values.
    """
    output: dict[Any, int] = {}
    for item in data:
        if item in output:
            output[item] += 1
        else:
            output[item] = 1
    return output


print(two_four_one(["a", "b", "f", "a", "c", "e", "a", "a", "b", "e", "f"]))
assert (two_four_one(["a", "b", "f", "a", "c", "e", "a", "a", "b", "e", "f"])) == {
    "a": 4,
    "b": 2,
    "f": 2,
    "c": 1,
    "e": 2,
}
assert (two_four_one([3, 4, 7, 5, 9, 3, 4, 5, 0, 3, 2, 3])) == {
    3: 4,
    4: 2,
    7: 1,
    5: 2,
    9: 1,
    0: 1,
    2: 1,
}


def two_four_two(one: Iterable[Any], two: Iterable[Any]):
    """
    Write a Python program to get the symmetric difference between two iterables, without filtering
    out duplicate values.
    """
    output = []
    for item in one:
        if item in two or item in output:
            continue
        output.append(item)
    for item in two:
        if item in one or item in output:
            continue
        output.append(item)
    return output


print(two_four_two([10, 20, 30], [10, 20, 40]))
assert (two_four_two([10, 20, 30], [10, 20, 40])) == [30, 40]


def two_four_three(data: list[Any], callback: Callable):
    """
    Write a Python program to check if a given function returns True for every element in a list.
    """
    return all(callback(item) for item in data)


print(two_four_three([4, 2, 3], lambda x: x > 1))
assert two_four_three([4, 2, 3], lambda x: x > 1) is True
assert two_four_three([4, 2, 3], lambda x: x < 1) is False
assert two_four_three([4, 2, 3], lambda x: x == 1) is False


def two_four_four(end: int, start=1, step=2):
    """
    Write a Python program to initialize a list containing the numbers in the specified range where
    start and end are inclusive and the ratio between two terms is step. Returns an error if step
    equals 1.
    """
    if step == 1:
        raise ValueError()
    output = []
    value = start
    while value <= end:
        output.append(value)
        value *= step
    return output


print(two_four_four(256))
assert two_four_four(256) == [1, 2, 4, 8, 16, 32, 64, 128, 256]
assert two_four_four(256, 3) == [3, 6, 12, 24, 48, 96, 192]
assert two_four_four(256, 1, 4) == [1, 4, 16, 64, 256]


def two_four_five(data: List[Sized]):
    """
    Write a Python program to that takes any number of iterable objects or objects with a length
    property and returns the longest one.
    """
    return sorted(data, key=len)[-1]


print(two_four_five(["this", "is", "a", "Green"]))
assert two_four_five(["this", "is", "a", "Green"]) == "Green"
assert two_four_five([[1, 2, 3], [1, 2], [1, 2, 3, 4, 5]]) == [1, 2, 3, 4, 5]
assert two_four_five([[1, 2, 3, 4], "Red"]) == [1, 2, 3, 4]


def two_four_six(data: list[Any], callback: Callable):
    """
    Write a Python program to check if a given function returns True for at least one element in the
    list.
    """
    return any(callback(item) for item in data)


print(two_four_six([0, 1, 2, 0], lambda x: x >= 2))
assert two_four_six([0, 1, 2, 0], lambda x: x >= 2) is True
assert two_four_six([5, 10, 20, 10], lambda x: x < 2) is False


def two_four_seven(one: Iterable, two: Iterable):
    """
    Write a Python program to calculate the difference between two iterables, without filtering
    duplicate values.
    """
    return [item for item in one if item not in two]


print(two_four_seven([1, 2, 3], [1, 2, 4]))
assert two_four_seven([1, 2, 3], [1, 2, 4]) == [3]


def two_four_eight(data: List[Any], callback: Callable):
    """
    Write a Python program to get the maximum value of a list, after mapping each element to a value
    using a given function.
    """
    return sorted(callback(item) for item in data)[-1]


print(two_four_eight([{"n": 4}, {"n": 2}, {"n": 8}, {"n": 6}], lambda v: v["n"]))
assert two_four_eight([{"n": 4}, {"n": 2}, {"n": 8}, {"n": 6}], lambda v: v["n"]) == 8


def two_four_nine(data: List[Any], callback: Callable):
    """
    Write a Python program to get the minimum value of a list, after mapping each element to a value
    using a given function.
    """
    return sorted(callback(item) for item in data)[0]


print(two_four_nine([{"n": 4}, {"n": 2}, {"n": 8}, {"n": 6}], lambda v: v["n"]))
assert two_four_nine([{"n": 4}, {"n": 2}, {"n": 8}, {"n": 6}], lambda v: v["n"]) == 2


def two_five_zero(data: List[Any], callback: Callable):
    """
    Write a Python program to calculate the sum of a list, after mapping each element to a value
    using the provided function.
    """
    return sum(callback(item) for item in data)


print(two_five_zero([{"n": 4}, {"n": 2}, {"n": 8}, {"n": 6}], lambda v: v["n"]))
assert two_five_zero([{"n": 4}, {"n": 2}, {"n": 8}, {"n": 6}], lambda v: v["n"]) == 20
