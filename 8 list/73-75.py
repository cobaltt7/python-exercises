from typing import Any


def seven_three(data: list[Any]):
    """
    Write a Python program to remove consecutive (following each other continuously) duplicates
    (elements) from a given list.
    """
    return [item for index, item in enumerate(data[:-1]) if item != data[index + 1]] + [
        data[-1]
    ]


print(seven_three([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]))
assert seven_three([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]) == [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    4,
]


def seven_four(data: list[Any]):
    """
    Write a Python program to pack consecutive duplicates of a given list of elements into sublists.
    """
    output = []
    for index, item in enumerate(data):
        if index == 0 or item != data[index - 1]:
            output.append([item])
        else:
            output[-1].append(item)
    return output


print(seven_four([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]))
assert seven_four([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]) == [
    [0, 0],
    [1],
    [2],
    [3],
    [4, 4],
    [5],
    [6, 6, 6],
    [7],
    [8],
    [9],
    [4, 4],
]


def seven_five(data: list[Any] | str):
    """
    Write a Python program to create a list reflecting the run-length encoding from a given list of
    integers or a given list of characters.
    """
    output = []
    for index, item in enumerate(data):
        if index == 0 or item != data[index - 1]:
            output.append([item])
        else:
            output[-1].append(item)
    return [[len(sublist), sublist[0]] for sublist in output]


print(seven_five("automatically"))
assert seven_five([1, 1, 2, 3, 4, 4.3, 5, 1]) == [
    [2, 1],
    [1, 2],
    [1, 3],
    [1, 4],
    [1, 4.3],
    [1, 5],
    [1, 1],
]
assert seven_five("automatically") == [
    [1, "a"],
    [1, "u"],
    [1, "t"],
    [1, "o"],
    [1, "m"],
    [1, "a"],
    [1, "t"],
    [1, "i"],
    [1, "c"],
    [1, "a"],
    [2, "l"],
    [1, "y"],
]
