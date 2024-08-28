from typing import Any


def one_one_one(data: list[Any], indicies: list[int]):
    """Write a Python program to access multiple elements at a specified index from a given list."""
    return [data[index] for index in indicies]


print(
    one_one_one(
        [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2], [0, 3, 5, 7, 10]
    )
)
assert one_one_one(
    [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2], [0, 3, 5, 7, 10]
) == [2, 4, 9, 2, 1]


def one_one_two(data: list[Any]):
    """Write a Python program to check whether a specified list is sorted or not."""
    return data == sorted(data)


print(one_one_two([1, 2, 4, 6, 8, 10, 12, 14, 16, 17]))
assert one_one_two([1, 2, 4, 6, 8, 10, 12, 14, 16, 17]) is True
assert one_one_two([1, 2, 4, 6, 8, 10, 12, 14, 17, 16]) is False
assert (
    one_one_two([2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]) is False
)


def one_one_three(data: list[dict]):
    """Write a Python program to remove duplicate dictionary from a given list."""
    return [dict(entry) for entry in {tuple(subdict.items()) for subdict in data}]


print(
    one_one_three(
        [
            {"Green": "#008000"},
            {"Black": "#000000"},
            {"Blue": "#0000FF"},
            {"Green": "#008000"},
        ]
    )
)
assert one_one_three(
    [
        {"Green": "#008000"},
        {"Black": "#000000"},
        {"Blue": "#0000FF"},
        {"Green": "#008000"},
    ]
) == [{"Green": "#008000"}, {"Black": "#000000"}, {"Blue": "#0000FF"}]
