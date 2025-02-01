def one_five_five(one: list[float], two: list[float]):
    """Write a Python program to add two given lists of different lengths, start from left."""
    is_one_longer = len(one) > len(two)
    longer = one if is_one_longer else two
    shorter = two if is_one_longer else one
    shorter_length = len(shorter)
    return [
        (shorter[index] + item) if index < shorter_length else item
        for index, item in enumerate(longer)
    ]


print(one_five_five([2, 4, 7, 0, 5, 8], [3, 3, -1, 7]))
assert one_five_five([2, 4, 7, 0, 5, 8], [3, 3, -1, 7]) == [5, 7, 6, 7, 5, 8]
assert one_five_five([1, 2, 3, 4, 5, 6], [2, 4, -3]) == [3, 6, 0, 4, 5, 6]


def one_five_six(one: list[float], two: list[float]):
    """Write a Python program to add two given lists of different lengths, start from right."""
    is_one_longer = len(one) > len(two)
    longer = (one if is_one_longer else two)[::-1]
    shorter = (two if is_one_longer else one)[::-1]
    shorter_length = len(shorter)
    return [
        (shorter[index] + item) if index < shorter_length else item
        for index, item in enumerate(longer)
    ][::-1]


print(one_five_six([2, 4, 7, 0, 5, 8], [3, 3, -1, 7]))
assert one_five_six([2, 4, 7, 0, 5, 8], [3, 3, -1, 7]) == [2, 4, 10, 3, 4, 15]
assert one_five_six([1, 2, 3, 4, 5, 6], [2, 4, -3]) == [1, 2, 3, 6, 9, 3]
