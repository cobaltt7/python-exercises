from typing import Any


def nine_five(data: list[list[str]]):
    """Write a Python program to sort each sublist of strings in a given list of lists."""
    return [sorted(sublist) for sublist in data]


print(
    nine_five([["green", "orange"], ["black", "white"], ["white", "black", "orange"]])
)
assert nine_five(
    [["green", "orange"], ["black", "white"], ["white", "black", "orange"]]
) == [["green", "orange"], ["black", "white"], ["black", "orange", "white"]]


def nine_six(lists: list[list[float]]):
    """Write a Python program to sort a given list of lists by length and value."""
    return sorted(sorted(lists), key=len)


print(nine_six([[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]))
assert nine_six([[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]) == [
    [0],
    [2],
    [0, 7],
    [1, 3],
    [9, 11],
    [13, 15, 17],
]


def nine_seven(data: list[list[Any]], min_value, max_value):
    """
    Write a Python program to remove sublists from a given list of lists, which are outside a given
    range.
    """
    output = []
    for sublist in data:
        filtered = [number for number in sublist if max_value >= number >= min_value]
        if filtered:
            output.append(filtered)
    return output


print(
    nine_seven(
        [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]], 13, 17
    )
)
assert nine_seven(
    [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]], 13, 17
) == [[13, 14, 15, 17]]
