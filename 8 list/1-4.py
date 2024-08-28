def one(data: list[float]):
    """Write a Python program to sum all the items in a list."""
    out = 0
    for number in data:
        out += number
    return out


print(one([1, 2, -8]))
assert one([1, 2, -8]) == -5


def two(data: list[float]):
    """Write a Python program to multiply all the items in a list."""
    out = 1
    for number in data:
        out *= number
    return out


print(two([1, 2, -8]))
assert two([1, 2, -8]) == -16


def three(data: list[float]):
    """Write a Python program to get the largest number from a list."""
    out = None
    for number in data:
        if out is None or out < number:
            out = number
    return out


print(three([1, 2, -8, 0]))
assert three([1, 2, -8, 0]) == 2


def four(data: list[float]):
    """Write a Python program to get the smallest number from a list."""
    out = None
    for number in data:
        if out is None or out > number:
            out = number
    return out


print(four([1, 2, -8]))
assert four([1, 2, -8, 0]) == -8
