from typing import Any, Sequence


def one_five_seven(data: list[Any]):
    """Write a Python program to interleave lists of varying lengths."""
    output = []
    for index in range(max(map(len, data))):
        for sublist in data:
            if index < len(sublist):
                output.append(sublist[index])
    return output


print(one_five_seven([[2, 4, 7, 0, 5, 8], [2, 5, 8], [0, 1], [3, 3, -1, 7]]))
assert one_five_seven([[2, 4, 7, 0, 5, 8], [2, 5, 8], [0, 1], [3, 3, -1, 7]]) == [
    2,
    2,
    0,
    3,
    4,
    5,
    1,
    3,
    7,
    8,
    -1,
    0,
    7,
    5,
    8,
]


def one_five_eight(data: list[Sequence[Any]]):
    """Write a Python program to find the maximum and minimum values in a given list of tuples."""
    numbers = sorted(
        item for sublist in data for item in sublist if isinstance(item, (float, int))
    )
    return (numbers[-1], numbers[0])


print(
    one_five_eight(
        [("V", 60), ("VI", 70), ("VII", 75), ("VIII", 72), ("IX", 78), ("X", 70)]
    )
)
assert one_five_eight(
    [("V", 60), ("VI", 70), ("VII", 75), ("VIII", 72), ("IX", 78), ("X", 70)]
) == (78, 60)

