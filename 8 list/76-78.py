from typing import Any


def seven_six(data: list[Any] | str):
    """
    Write a Python program to create a list reflecting the modified run-length encoding from a given
    list of integers or a given list of characters.
    """
    output = []
    for index, item in enumerate(data):
        if index == 0 or item != data[index - 1]:
            output.append([item])
        else:
            output[-1].append(item)
    return [
        sublist[0] if len(sublist) == 1 else [len(sublist), sublist[0]]
        for sublist in output
    ]


print(seven_six([1, 1, 2, 3, 4, 4, 5, 1]))
assert seven_six([1, 1, 2, 3, 4, 4, 5, 1]) == [[2, 1], 2, 3, [2, 4], 5, 1]
assert seven_six("aabcddddadnss") == [
    [2, "a"],
    "b",
    "c",
    [4, "d"],
    "a",
    "d",
    "n",
    [2, "s"],
]


def seven_seven(data: list[int | list[Any]]):
    """Write a Python program to decode a run-length encoded given list."""
    output = []
    for item in data:
        if isinstance(item, list):
            output += [item[1]] * item[0]
        else:
            output.append(item)
    return output


print(seven_seven([[2, 1], 2, 3, [2, 4], 5, 1]))
assert seven_seven([[2, 1], 2, 3, [2, 4], 5, 1]) == [1, 1, 2, 3, 4, 4, 5, 1]


def seven_eight(data: list[Any], length: int):
    """
    Write a Python program to split a given list into two parts where the length of the first part
    of the list is given.
    """
    return (data[:length], data[length:])


print(seven_eight([1, 1, 2, 3, 4, 4, 5, 1], 3))
assert seven_eight([1, 1, 2, 3, 4, 4, 5, 1], 3) == ([1, 1, 2], [3, 4, 4, 5, 1])
