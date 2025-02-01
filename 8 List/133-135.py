from typing import Any


def one_three_three(one: list[Any], two: list[Any]):
    """
    Write a Python program to check if two lists have the same elements in them in same order or
    not.
    """
    index = -1
    for item in one:
        if item not in two:
            continue

        found = two.index(item)
        if found < index:
            return False
        index = found
    return True


print(
    one_three_three(
        ["red", "green", "black", "orange"], ["red", "pink", "green", "white", "black"]
    )
)
assert (
    one_three_three(
        ["red", "green", "black", "orange"], ["red", "pink", "green", "white", "black"]
    )
    is True
)
assert (
    one_three_three(
        ["red", "green", "black", "orange"], ["white", "orange", "pink", "black"]
    )
    is False
)
assert (
    one_three_three(
        ["red", "pink", "green", "white", "black"], ["white", "orange", "pink", "black"]
    )
    is False
)


def one_three_four(one: list[Any], two: list[Any]):
    """
    Write a Python program to find the difference between two lists including duplicate elements.
    """
    output = one[::]
    for item in two:
        output.remove(item)
    return output


print(one_three_four([1, 1, 2, 3, 3, 4, 4, 5, 6, 7], [1, 1, 2, 4, 5, 6]))
assert one_three_four([1, 1, 2, 3, 3, 4, 4, 5, 6, 7], [1, 1, 2, 4, 5, 6]) == [
    3,
    3,
    4,
    7,
]


def one_three_five(data: list[Any]):
    """
    Write a Python program to iterate over all pairs of consecutive items in a given list.
    """
    return [(data[index], item) for index, item in enumerate(data[1:])]


print(one_three_five([1, 1, 2, 3, 3, 4, 4, 5]))
assert one_three_five([1, 1, 2, 3, 3, 4, 4, 5]) == [
    (1, 1),
    (1, 2),
    (2, 3),
    (3, 3),
    (3, 4),
    (4, 4),
    (4, 5),
]
