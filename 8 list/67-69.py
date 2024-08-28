from typing import Any


def six_seven(data: list[float], number: float):
    """
    Write a Python program to find all the values in a list that are greater than a specified
    number.
    """
    return [item for item in data if item > number]


print(six_seven([220, 330, 500], 200))
assert six_seven([220, 330, 500], 200) == [220, 330, 500]
assert six_seven([12, 17, 21], 25) == []


def six_eight(data: list[Any], item: Any):
    """Write a Python program to extend a list without append."""
    data += [item]
    return data


print(six_eight([40, 50, 60], 70))
assert six_eight([40, 50, 60], 70) == [40, 50, 60, 70]


def six_nine(data: list[list[Any]]):
    """Write a Python program to remove duplicates from a list of lists."""
    seen = []
    output = []
    for sublist in data:
        new_sublist = []
        for item in sublist:
            if item not in seen:
                seen.append(item)
                new_sublist.append(item)
        if new_sublist:
            output.append(new_sublist)
    return output


print(six_nine([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]))
assert six_nine([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]) == [
    [10, 20],
    [40],
    [30, 56, 25],
    [33],
]
