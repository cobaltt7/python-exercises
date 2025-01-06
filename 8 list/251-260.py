from typing import Any


def two_five_one(length: int, item: Any):
    """Write a Python program that fills a list with the specified value."""
    return [item for _ in range(length)]


print(two_five_one(7, 0))
assert two_five_one(7, 0) == [0, 0, 0, 0, 0, 0, 0]
assert two_five_one(8, 3) == [3, 3, 3, 3, 3, 3, 3, 3]
assert two_five_one(5, -2) == [-2, -2, -2, -2, -2]
assert two_five_one(5, 3.2) == [3.2, 3.2, 3.2, 3.2, 3.2]


def two_five_two(data: list[float], count: int = 1):
    """Write a Python program to get the n maximum elements from a given list of numbers."""
    return sorted(data, reverse=True)[:count]


print(two_five_two([1, 2, 3]))
assert two_five_two([1, 2, 3]) == [3]
assert two_five_two([1, 2, 3], 2) == [3, 2]
assert two_five_two([-2, -3, -1, -2, -4, 0, -5], 3) == [0, -1, -2]
assert two_five_two([2.2, 2, 3.2, 4.5, 4.6, 5.2, 2.9], 2) == [5.2, 4.6]


def two_five_three(data: list[float], count: int = 1):
    """Write a Python program to get the n minimum elements from a given list of numbers."""
    return sorted(data)[:count]


print(two_five_three([1, 2, 3]))
assert two_five_three([1, 2, 3]) == [1]
assert two_five_three([1, 2, 3], 2) == [1, 2]
assert two_five_three([-2, -3, -1, -2, -4, 0, -5], 3) == [-5, -4, -3]
assert two_five_three([2.2, 2, 3.2, 4.5, 4.6, 5.2, 2.9], 2) == [2, 2.2]


def two_five_four(data: list[float], weights: list[float]):
    """Write a  Python program to get the weighted average of two or more numbers."""
    return sum(data[index] * weight for index, weight in enumerate(weights)) / sum(
        weights
    )


print(two_five_four([10, 50, 40], [2, 5, 3]))
assert two_five_four([10, 50, 40], [2, 5, 3]) == 39.0
assert two_five_four([82, 90, 76, 83], [0.2, 0.35, 0.45, 32]) == 82.97272727272727


def two_five_five(data: list[Any]):
    """Write a Python program to perform a deep flattening of a list."""
    return [item for items in data for item in items]


print(two_five_five([1, [2], [[3], [4], 5], 6]))
assert two_five_five([1, [2], [[3], [4], 5], 6]) == [1, 2, 3, 4, 5, 6]
assert two_five_five([[[1, 2, 3], [4, 5]], 6]) == [1, 2, 3, 4, 5, 6]


def two_five_six(data: list[Any]):
    """Write a Python program to get the powerset of a given iterable."""
    output = [()]
    for index in range(len(data)):
        for subindex in range(index + 1):
            output.append(set(data[subindex : index + 1]))
    return output


print(two_five_six([1, 2]))
assert two_five_six([1, 2]) == [(), (1,), (2,), (1, 2)]
assert two_five_six([1, 2, 3, 4]) == [
    (),
    (1,),
    (2,),
    (3,),
    (4,),
    (1, 2),
    (1, 3),
    (1, 4),
    (2, 3),
    (2, 4),
    (3, 4),
    (1, 2, 3),
    (1, 2, 4),
    (1, 3, 4),
    (2, 3, 4),
    (1, 2, 3, 4),
]


def two_five_seven(one: list[Any], two: list[Any]):
    """
    Write a Python program to check if two given lists contain the same elements regardless of
    order.
    """
    for item in one:
        if item not in two:
            return False
    for item in two:
        if item not in one:
            return False
    return True


print(two_five_seven([1, 2, 4], [2, 4, 1]))
assert two_five_seven([1, 2, 4], [2, 4, 1]) is True
assert two_five_seven([1, 2, 3], [1, 2, 3]) is True
assert two_five_seven([1, 2, 3], [1, 2, 4]) is False


def two_five_eight(data: dict[str, Any]):
    """Write a Python program to create a flat list of all the keys in a flat dictionary."""
    return list(data.keys())


print(two_five_eight({"Laura": 10, "Spencer": 11, "Bridget": 9, "Howard ": 10}))
assert two_five_eight({"Laura": 10, "Spencer": 11, "Bridget": 9, "Howard ": 10}) == [
    "Laura",
    "Spencer",
    "Bridget",
    "Howard ",
]


def two_five_nine(data: list[Any], callback: callable = lambda x: x):
    """
    Write a Python program to check if a given function returns True for at least one element in the
    list.
    """
    return any(callback(item) for items in data)


print(two_five_nine([1, 0, 2, 3], lambda x: x <= 3))
assert two_five_nine([1, 0, 2, 3], lambda x: x <= 3) is True
assert two_five_nine([1, 0, 2, 3], lambda x: x > 0) is False
assert two_five_nine([2, 2, 4, 4]) is True


def two_six_zero(one: list[Any], two: list[Any]):
    """
    Write a Python program to check if all the elements of a list are included in another given
    list.
    """
    return all(item in one for item in two)


print(two_six_zero([10, 20, 30, 40, 50, 60], [20, 40]))
assert two_six_zero([10, 20, 30, 40, 50, 60], [20, 40]) is True
assert two_six_zero([10, 20, 30, 40, 50, 60], [20, 80]) is False
