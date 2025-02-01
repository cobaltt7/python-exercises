from typing import Any


def seven_zero(data: list[str], start: str):
    """Write a Python program to find the items starts with specific character from a given list."""
    return [item for item in data if item[0] == start]


print(
    seven_zero(
        ["abcd", "abc", "bcd", "bkie", "cder", "cdsw", "sdfsd", "dagfa", "acjd"], "a"
    )
)
assert seven_zero(
    ["abcd", "abc", "bcd", "bkie", "cder", "cdsw", "sdfsd", "dagfa", "acjd"], "a"
) == ["abcd", "abc", "acjd"]
assert seven_zero(
    ["abcd", "abc", "bcd", "bkie", "cder", "cdsw", "sdfsd", "dagfa", "acjd"], "d"
) == ["dagfa"]
assert (
    seven_zero(
        ["abcd", "abc", "bcd", "bkie", "cder", "cdsw", "sdfsd", "dagfa", "acjd"], "w"
    )
    == []
)


def seven_one(data: list[dict]):
    """Write a Python program to check if all dictionaries in a list are empty or not."""
    return not any(data)


print(seven_one([{}, {}, {}]))
assert seven_one([{}, {}, {}]) is True
assert seven_one([{1: 2}, {}, {}]) is False


def seven_two(data: list[Any]):
    """Write a Python program to flatten a given nested list structure."""
    output = []
    for item in data:
        if isinstance(item, list):
            output += seven_two(item)
        else:
            output.append(item)
    return output


print(seven_two([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]))
assert seven_two([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]) == [
    0,
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80,
    90,
    100,
    110,
    120,
]
assert seven_two([0, [10, [[20], 30], 40, 50, [60], 70, 80], [90, 100, 110, 120]]) == [
    0,
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80,
    90,
    100,
    110,
    120,
]
