from math import sqrt


def thirtyOne(data):
    """Write a Python program to find the coordinates of a triangle with given side lengths."""
    y = ((data[0] ** 2) + (data[2] ** 2) - (data[1] ** 2)) / (2 * data[0])
    return [[0.0, 0.0], [data[0], 0.0], [y, sqrt(abs((data[2] ** 2) - (y**2)))]]


def thirtyTwo(data):
    """
    Write a Python program to rescale and shift numbers in a given list, so that they cover the
    range [0, 1].
    """

    small = min(data)
    big = max(data) - small
    return list(map(lambda number: (number - small) / big, data))


assert thirtyOne([3, 4, 5]) == [[0.0, 0.0], [3, 0.0], [3.0, 4.0]]
assert thirtyOne([5, 6, 7]) == [[0.0, 0.0], [5, 0.0], [3.8, 5.878775382679628]]

assert thirtyTwo([18.5, 17.0, 18.0, 19.0, 18.0]) == [0.75, 0.0, 0.5, 1.0, 0.5]
assert thirtyTwo([13.0, 17.0, 17.0, 15.5, 2.94]) == [
    0.7155049786628734,
    1.0,
    1.0,
    0.8933143669985776,
    0.0,
]
