from typing import Any, Callable
from math import floor, ceil


def two_two_six(one: list[Any], two: list[Any], callback: Callable):
    """
    Write a Python program to get a list of elements that exist in both lists, after applying the
    provided function to each list element of both.
    """
    search_array = set(map(callback, two))
    output = []
    for item in one:
        if callback(item) in search_array:
            output.append(item)
    return output


print(two_two_six([2.1, 1.2], [2.3, 3.4], floor))
assert two_two_six([2.1, 1.2], [2.3, 3.4], floor) == [2.1]


def two_two_seven(
    one: list[Any], two: list[Any], callback: Callable, both: bool = True
):
    """
    Write a Python program to get the symmetric difference between two lists, after applying the
    provided function to each list element of both.
    """
    if both:
        return two_two_seven(one, two, callback, False) + two_two_seven(
            two, one, callback, False
        )
    search_array = set(map(callback, two))
    output = []
    for item in one:
        if callback(item) not in search_array:
            output.append(item)
    return output


print(two_two_seven([2.1, 1.2], [2.3, 3.4], floor))
assert two_two_seven([2.1, 1.2], [2.3, 3.4], floor) == [1.2, 3.4]


def two_two_eight(one: list[Any], two: list[Any], callback: Callable):
    """
    Write a Python program to get every element that exists in any of the two given lists once,
    after applying the provided function to each element of both.
    """
    output = set()
    seen = set()
    for item in one + two:
        processed = callback(item)
        if processed not in seen:
            output.add(item)
            seen.add(processed)
    return output


print(two_two_eight([4.1], [2.2, 4.3], floor))
assert (two_two_eight([4.1], [2.2, 4.3], floor)) == {2.2, 4.1}


def two_two_nine(data: list[Any], callback: Callable):
    """
    Write a Python program to find the index of the first element in the given list that satisfies
    the provided testing function.
    """
    for index, item in enumerate(data):
        if callback(item):
            return index
    return None


print(two_two_nine([1, 2, 3, 4], lambda n: n % 2 == 1))
assert (two_two_nine([1, 2, 3, 4], lambda n: n % 2 == 1)) == 0


def two_three_zero(data: list[Any], callback: Callable):
    """
    Write a Python program to find the indexes of all elements in the given list that satisfy the
    provided testing function.
    """
    return [index for index, item in enumerate(data) if callback(item)]


print(two_three_zero([1, 2, 3, 4], lambda n: n % 2 == 1))
assert (two_three_zero([1, 2, 3, 4], lambda n: n % 2 == 1)) == [0, 2]


def two_three_one(data: list[Any], filter_list: list[bool]):
    """
    Write a Python program to split values into two groups, based on the result of the given filter
    list.
    """
    one = []
    two = []
    for index, item in enumerate(data):
        if filter_list[index]:
            one.append(item)
        else:
            two.append(item)
    return [one, two]


print(two_three_one(["red", "green", "blue", "pink"], [True, True, False, True]))
assert (two_three_one(["red", "green", "blue", "pink"], [True, True, False, True])) == [
    ["red", "green", "pink"],
    ["blue"],
]


def two_three_two(data: list[Any], size: int):
    """Write a Python program to chunk a given list into smaller lists of a specified size."""
    index = 0
    output = []
    while index < len(data):
        output.append(data[index : index + size])
        index += size
    return output


print(two_three_two([1, 2, 3, 4, 5, 6, 7, 8], 3))
assert (two_three_two([1, 2, 3, 4, 5, 6, 7, 8], 3)) == [[1, 2, 3], [4, 5, 6], [7, 8]]


def two_three_three(data: list[Any], count: int):
    """Write a Python program to chunk a given list into n smaller lists."""
    size = ceil(len(data) / count)
    index = 0
    output = []
    while index < len(data):
        output.append(data[index : index + size])
        index += size
    return output


print(two_three_three([1, 2, 3, 4, 5, 6, 7], 4))
assert (two_three_three([1, 2, 3, 4, 5, 6, 7], 4)) == [[1, 2], [3, 4], [5, 6], [7]]


def two_three_four(data: int):
    """Write a Python program to convert a given number (integer) to a list of digits."""
    return list(map(int, str(data)))


print(two_three_four(123))
assert (two_three_four(123)) == [1, 2, 3]
assert (two_three_four(1347823)) == [1, 3, 4, 7, 8, 2, 3]


def two_three_five(data: list[Any], callback: Callable):
    """
    Write a Python program to find the index of the last element in the given list that satisfies
    the provided testing function.
    """
    for index, item in enumerate(data[::-1]):
        if callback(item):
            return len(data) - 1 - index
    return None


print(two_three_five([1, 2, 3, 4], lambda n: n % 2 == 1))
assert two_three_five([1, 2, 3, 4], lambda n: n % 2 == 1) == 2
