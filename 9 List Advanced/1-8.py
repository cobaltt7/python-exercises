from typing import Any


def one(data: list[Any], start: int, end: int):
    """Write a Python function to reverse a list at a specific location."""
    return (
        data[:start]
        + data[end : (None if start == 0 else start - 1) : -1]
        + data[end + 1 :]
    )


print(one([10, 20, 50, 40, 30, 60, 80, 70], 0, 7))
assert one([10, 20, 30, 40, 50, 60, 70, 80], 2, 4) == [10, 20, 50, 40, 30, 60, 70, 80]
assert one([10, 20, 50, 40, 30, 60, 70, 80], 6, 7) == [10, 20, 50, 40, 30, 60, 80, 70]
assert one([10, 20, 50, 40, 30, 60, 80, 70], 0, 7) == [70, 80, 60, 30, 40, 50, 20, 10]


def two(data: list[float]):
    """
    Write a Python function find the length of the longest increasing sub-sequence in a
    list.
    """
    output = 0
    last = 0.0
    current = 0
    for item in data:
        if current == 0:
            current = 1
        elif item > last:
            current += 1
        else:
            output = max(output, current)
            current = 0
        last = item
    return max(current, output)


print(two([10, 20, 30, 40, 50, 30, 30, 20]))
assert two([10, 20, 30, 40, 50, 60, 70, 80]) == 8
assert two([10, 20, 30, 40, 50, 30, 30, 20]) == 5
assert two([-1, -2, -3, -4, -5, -11, -12, -13]) == 1


def three(data: list[Any]):
    """
    Write a Python function that finds all the permutations of the members of a list.

    In mathematics, the notion of permutation relates to the act of arranging all the
    members of a set into some sequence or order, or if the set is already ordered,
    rearranging (reordering) its elements, a process called permuting. These differ
    from combinations, which are selections of some members of a set where order is
    disregarded
    """
    if len(data) == 0:
        return [[]]

    output = []

    for index, number in enumerate(data):
        for perm in three(data[:index] + data[index + 1 :]):
            output.append([number, *perm])

    return output


print(three([1, 2, 3, 4]))
assert three([1, 2, 3, 4]) == [
    [1, 2, 3, 4],
    [1, 2, 4, 3],
    [1, 3, 2, 4],
    [1, 3, 4, 2],
    [1, 4, 2, 3],
    [1, 4, 3, 2],
    [2, 1, 3, 4],
    [2, 1, 4, 3],
    [2, 3, 1, 4],
    [2, 3, 4, 1],
    [2, 4, 1, 3],
    [2, 4, 3, 1],
    [3, 1, 2, 4],
    [3, 1, 4, 2],
    [3, 2, 1, 4],
    [3, 2, 4, 1],
    [3, 4, 1, 2],
    [3, 4, 2, 1],
    [4, 1, 2, 3],
    [4, 1, 3, 2],
    [4, 2, 1, 3],
    [4, 2, 3, 1],
    [4, 3, 1, 2],
    [4, 3, 2, 1],
]

assert three([-100, -300, 0]) == [
    [-100, -300, 0],
    [-100, 0, -300],
    [-300, -100, 0],
    [-300, 0, -100],
    [0, -100, -300],
    [0, -300, -100],
]


def four(data: list[float], k: int):
    """Write a Python function to find the kth smallest element in a list."""
    return sorted(data)[k - 1]


print(four([1, 2, 4, 3, 5, 4, 6, 9, 2, 1], 1))
assert four([1, 2, 4, 3, 5, 4, 6, 9, 2, 1], 1) == 1
assert four([1, 2, 4, 3, 5, 4, 6, 9, 2, 1], 2) == 1
assert four([1, 2, 4, 3, 5, 4, 6, 9, 2, 1], 3) == 2
assert four([1, 2, 4, 3, 5, 4, 6, 9, 2, 1], 4) == 2
assert four([1, 2, 4, 3, 5, 4, 6, 9, 2, 1], 5) == 3
assert four([1, 2, 4, 3, 5, 4, 6, 9, 2, 1], 6) == 4
assert four([1, 2, 4, 3, 5, 4, 6, 9, 2, 1], 7) == 4
assert four([1, 2, 4, 3, 5, 4, 6, 9, 2, 1], 8) == 5
assert four([1, 2, 4, 3, 5, 4, 6, 9, 2, 1], 9) == 6
assert four([1, 2, 4, 3, 5, 4, 6, 9, 2, 1], 10) == 9


def five(data: list[float], k: int):
    """Write a Python function to find the kth largest element in a list."""
    return sorted(data, reverse=True)[k - 1]


print(five([1, 2, 4, 3, 5, 4, 6, 9, 2, 1], 1))
assert five([1, 2, 4, 3, 5, 4, 6, 9, 2, 1], 1) == 9
assert five([1, 2, 4, 3, 5, 4, 6, 9, 2, 1], 2) == 6
assert five([1, 2, 4, 3, 5, 4, 6, 9, 2, 1], 3) == 5
assert five([1, 2, 4, 3, 5, 4, 6, 9, 2, 1], 4) == 4
assert five([1, 2, 4, 3, 5, 4, 6, 9, 2, 1], 5) == 4
assert five([1, 2, 4, 3, 5, 4, 6, 9, 2, 1], 6) == 3
assert five([1, 2, 4, 3, 5, 4, 6, 9, 2, 1], 7) == 2
assert five([1, 2, 4, 3, 5, 4, 6, 9, 2, 1], 8) == 2
assert five([1, 2, 4, 3, 5, 4, 6, 9, 2, 1], 9) == 1
assert five([1, 2, 4, 3, 5, 4, 6, 9, 2, 1], 10) == 1


def six(data: list[Any]):
    """
    Write a Python function to check if a list is a palindrome or not. Return true
    otherwise false.
    """
    return data == data[::-1]


print(six([1, 2, 4, 3, 5, 4, 6, 9, 2, 1]))
assert six([1, 2, 4, 3, 5, 4, 6, 9, 2, 1]) is False
assert six([1, 2, 2, 1]) is True
assert six(["Red", "Green", "Blue"]) is False
assert six(["Red", "Green", "Red"]) is True


def seven(list_one: set[Any], list_two: set[Any]):
    """Write a Python a function to find the union and intersection of two lists."""
    return (
        set([*list_one, *list_two]),
        set(item for item in list_one if item in list_two),
    )


print(seven({1, 2, 3, 4, 5}, {3, 4, 5, 6, 7, 8}))
assert seven({1, 2, 3, 4, 5}, {3, 4, 5, 6, 7, 8}) == (
    {1, 2, 3, 4, 5, 6, 7, 8},
    {3, 4, 5},
)
assert seven({"Red", "Green", "Blue"}, {"Red", "White", "Pink", "Black"}) == (
    {"Pink", "Blue", "White", "Black", "Red", "Green"},
    {"Red"},
)


def eight(data: list[Any]):
    """
    Write a Python function to remove duplicates from a list while preserving the order.
    """
    return [item for index, item in enumerate(data) if data.index(item) == index]


print(eight([1, 2, 4, 3, 5, 4, 6, 9, 2, 1]))
assert eight([1, 2, 4, 3, 5, 4, 6, 9, 2, 1]) == [1, 2, 4, 3, 5, 6, 9]
assert eight(
    ["a", "a", "b", "a", "a", "c", "c", "c", "d", "e", "a", "b", "b", "b"]
) == ["a", "b", "c", "d", "e"]
