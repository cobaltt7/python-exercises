def fortyFive(data):
    """Write a Python program to find all even palindromes up to n."""
    return [n for n in range(data) if (n % 2 == 0) and (str(n) == str(n)[::-1])]


def fortySix(data):
    """
    Given an array of numbers representing a branch on a binary tree, write a Python program to
    find the minimum even value and its index. In the case of a tie, return the smallest index. If
    there are no even numbers, the answer is [].
    """
    filtered = [n for n in enumerate(data) if n[1] % 2 == 0]
    entry = sorted(
        sorted(filtered, key=lambda entry: entry[0]), key=lambda entry: entry[1]
    )
    return [entry[0][1], entry[0][0]] if entry else []


def fortySeven(data):
    """
    Write a Python program to filter for numbers in a given list whose sum of digits is > 0, where
    the first digit can be negative.
    """

    def get_digits(n):
        digits = list(map(int, str(abs(n))))
        if n < 0:
            digits[0] = -1 * digits[0]
        return digits

    return [n for n in data if sum(get_digits(n)) > 0]


print(fortyFive(50))
assert fortyFive(50) == [0, 2, 4, 6, 8, 22, 44]
assert fortyFive(100) == [0, 2, 4, 6, 8, 22, 44, 66, 88]
assert fortyFive(500) == [
    0,
    2,
    4,
    6,
    8,
    22,
    44,
    66,
    88,
    202,
    212,
    222,
    232,
    242,
    252,
    262,
    272,
    282,
    292,
    404,
    414,
    424,
    434,
    444,
    454,
    464,
    474,
    484,
    494,
]
assert fortyFive(2000) == [
    0,
    2,
    4,
    6,
    8,
    22,
    44,
    66,
    88,
    202,
    212,
    222,
    232,
    242,
    252,
    262,
    272,
    282,
    292,
    404,
    414,
    424,
    434,
    444,
    454,
    464,
    474,
    484,
    494,
    606,
    616,
    626,
    636,
    646,
    656,
    666,
    676,
    686,
    696,
    808,
    818,
    828,
    838,
    848,
    858,
    868,
    878,
    888,
    898,
]

print(fortySix([1, 9, 4, 6, 10, 11, 14, 8]))
assert fortySix([1, 9, 4, 6, 10, 11, 14, 8]) == [4, 2]
assert fortySix([1, 7, 4, 4, 9, 2]) == [2, 5]
assert fortySix([1, 7, 7, 5, 9]) == []

print(fortySeven([11, -6, -103, -200]))
assert fortySeven([11, -6, -103, -200]) == [11, -103]
assert fortySeven([1, 7, -4, 4, -9, 2]) == [1, 7, 4, 2]
assert fortySeven([10, -11, -71, -13, 14, -32]) == [10, -13, 14]
