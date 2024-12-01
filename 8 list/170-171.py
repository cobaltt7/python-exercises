from typing import Any


def one_seven_zero(data: list[Any], item: Any, index: int):
    """Write a Python program to insert an element in a given list after every nth position."""
    start = data[:index]
    if len(data) < index:
        return start
    return start + [item] + one_seven_zero(data[index:], item, index)


print(one_seven_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "a", 2))
assert one_seven_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "a", 2) == [
    1,
    2,
    "a",
    3,
    4,
    "a",
    5,
    6,
    "a",
    7,
    8,
    "a",
    9,
    0,
    "a",
]
assert one_seven_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "b", 4) == [
    1,
    2,
    3,
    4,
    "b",
    5,
    6,
    7,
    8,
    "b",
    9,
    0,
]


def one_seven_one(data: list[list[str]]):
    """Write a Python program to concatenate element-wise three given lists."""
    output = []
    for index in range(max(map(len, data))):
        output.append("")
        for sublist in data:
            if index < len(sublist):
                output[-1] += sublist[index]
    return output


print(
    one_seven_one(
        [
            ["0", "1", "2", "3", "4"],
            ["red", "green", "black", "blue", "white"],
            ["100", "200", "300", "400", "500"],
        ]
    )
)
assert one_seven_one(
    [
        ["0", "1", "2", "3", "4"],
        ["red", "green", "black", "blue", "white"],
        ["100", "200", "300", "400", "500"],
    ]
) == ["0red100", "1green200", "2black300", "3blue400", "4white500"]
