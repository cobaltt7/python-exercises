def one_seven_four(data: list[float], add: float):
    """Write a Python program to add a number to each element in a given list of numbers."""
    return [item + add for item in data]


print(one_seven_four([3, 8, 9, 4, 5, 0, 5, 0, 3], 3))
assert one_seven_four([3, 8, 9, 4, 5, 0, 5, 0, 3], 3) == [6, 11, 12, 7, 8, 3, 8, 3, 6]

assert one_seven_four([3.2, 8, 9.9, 4.2, 5, 0.1, 5, 3.11, 0], 0.51) == [
    3.71,
    8.51,
    10.41,
    4.71,
    5.51,
    0.61,
    5.51,
    3.62,
    0.51,
]


def one_seven_five(data: list[tuple[float, float]]):
    """
    Write a Python program to find the minimum and maximum value for each tuple position in a given
    list of tuples.
    """
    count = range(len(data[0]))
    return (
        [max(item[index] for item in data) for index in count],
        [min(item[index] for item in data) for index in count],
    )


print(one_seven_five([(2, 3), (2, 4), (0, 6), (7, 1)]))
assert one_seven_five([(2, 3), (2, 4), (0, 6), (7, 1)]) == ([7, 6], [0, 1])
