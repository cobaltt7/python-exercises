from typing import Any


def one_three_nine(data: list[str]):
    """Write a Python program to sort a given list of strings(numbers) numerically."""
    return sorted(map(float, data))


print(one_three_nine(["4", "12", "45", "7", "0", "100", "200", "-12", "-500"]))
assert one_three_nine(["4", "12", "45", "7", "0", "100", "200", "-12", "-500"]) == [
    -500,
    -12,
    0,
    4,
    7,
    12,
    45,
    100,
    200,
]


def one_four_zero(data: list[list[Any]], index: int):
    """Write a Python program to remove the specific item from a given list of lists."""
    return [sublist[: index - 1] + sublist[index:] for sublist in data]


print(
    one_four_zero(
        [
            ["Red", "Maroon", "Yellow", "Olive"],
            ["#FF0000", "#800000", "#FFFF00", "#808000"],
            ["rgb(255,0,0)", "rgb(128,0,0)", "rgb(255,255,0)", "rgb(128,128,0)"],
        ],
        1,
    )
)
assert one_four_zero(
    [
        ["Red", "Maroon", "Yellow", "Olive"],
        ["#FF0000", "#800000", "#FFFF00", "#808000"],
        ["rgb(255,0,0)", "rgb(128,0,0)", "rgb(255,255,0)", "rgb(128,128,0)"],
    ],
    1,
) == [
    ["Maroon", "Yellow", "Olive"],
    ["#800000", "#FFFF00", "#808000"],
    ["rgb(128,0,0)", "rgb(255,255,0)", "rgb(128,128,0)"],
]
assert one_four_zero(
    [
        ["Red", "Maroon", "Yellow", "Olive"],
        ["#FF0000", "#800000", "#FFFF00", "#808000"],
        ["rgb(255,0,0)", "rgb(128,0,0)", "rgb(255,255,0)", "rgb(128,128,0)"],
    ],
    2,
) == [
    ["Red", "Yellow", "Olive"],
    ["#FF0000", "#FFFF00", "#808000"],
    ["rgb(255,0,0)", "rgb(255,255,0)", "rgb(128,128,0)"],
]
assert one_four_zero(
    [
        ["Red", "Maroon", "Yellow", "Olive"],
        ["#FF0000", "#800000", "#FFFF00", "#808000"],
        ["rgb(255,0,0)", "rgb(128,0,0)", "rgb(255,255,0)", "rgb(128,128,0)"],
    ],
    4,
) == [
    ["Red", "Maroon", "Yellow"],
    ["#FF0000", "#800000", "#FFFF00"],
    ["rgb(255,0,0)", "rgb(128,0,0)", "rgb(255,255,0)"],
]


def one_four_one(data: list[Any]):
    """Write a Python program to remove empty lists from a given list of lists."""
    return [sublist for sublist in data if sublist != []]


print(one_four_one([[], [], [], "Red", "Green", [1, 2], "Blue", [], []]))
assert one_four_one([[], [], [], "Red", "Green", [1, 2], "Blue", [], []]) == [
    "Red",
    "Green",
    [1, 2],
    "Blue",
]
