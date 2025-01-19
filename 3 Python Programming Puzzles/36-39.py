def thirtySix(data):
    """Write a Python program to find the largest k numbers from a given list of numbers."""
    thirtySix.k += 1
    return sorted(data, reverse=True)[: thirtySix.k]


def thirtySeven(data):
    """
    Write a Python program to find the largest integer divisor of a number n that is less than n.
    """
    for i in range(2, data + 1):
        divisor = data / i
        if divisor.is_integer():
            return divisor


def thirtyEight(data):
    """Write a Python program to sort the numbers in a given list by the sum of their digits."""

    def sum_digits(number):
        return sum(map(int, str(number)))

    return list(sorted(data, key=sum_digits))


def thirtyNine(data):
    """
    Write a Python program to determine which triples sum to zero from a given list of lists.
    """
    return list(map(lambda tuple: sum(tuple) == 0, data))


thirtySix.k = 0
assert thirtySix([1, 2, 3, 4, 5, 5, 3, 6, 2]) == [6]
assert thirtySix([1, 2, 3, 4, 5, 5, 3, 6, 2]) == [6, 5]
assert thirtySix([1, 2, 3, 4, 5, 5, 3, 6, 2]) == [6, 5, 5]
assert thirtySix([1, 2, 3, 4, 5, 5, 3, 6, 2]) == [6, 5, 5, 4]
assert thirtySix([1, 2, 3, 4, 5, 5, 3, 6, 2]) == [6, 5, 5, 4, 3]

assert thirtySeven(18) == 9
assert thirtySeven(100) == 50
assert thirtySeven(102) == 51
assert thirtySeven(500) == 250
assert thirtySeven(1000) == 500
assert thirtySeven(6500) == 3250

assert thirtyEight([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [
    10,
    11,
    20,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
]
assert thirtyEight([23, 2, 9, 34, 8, 9, 10, 74]) == [10, 2, 23, 34, 8, 9, 9, 74]

assert thirtyNine(
    [[1343532, -2920635, 332], [-27, 18, 9], [4, 0, -4], [2, 2, 2], [-20, 16, 4]]
) == [False, True, True, False, True]
assert thirtyNine([[1, 2, -3], [-4, 0, 4], [0, 1, -5], [1, 1, 1], [-2, 4, -1]]) == [
    True,
    True,
    False,
    False,
    False,
]
