from math import ceil


def eighty(flouts):
    """
    Write a Python program to round each float in a given list of numbers up to the next integer
    and return the running total of the integer squares.
    """
    ints = list(map(lambda number: ceil(number) ** 2, flouts))
    return [sum(ints[: entry[0] + 1]) for entry in enumerate(ints)]


print(eighty([2.6, 3.5, 6.7, 2.3, 5.6]))
assert eighty([2.6, 3.5, 6.7, 2.3, 5.6]) == [9, 25, 74, 83, 119]
assert eighty([301.1, 401.4, -23.1, 13554122.0, 10201.0101, 10000000.0]) == [
    91204,
    252808,
    253337,
    183714223444221,
    183714327525025,
    283714327525025,
]


def eightyOne(data):
    """
    Write a Python program to calculate the average of the numbers a through b (b not included)
    rounded to the nearest integer, in binary (or -1 if there are no such numbers).
    """
    numbers = range(*data)
    return bin(round(sum(numbers) / len(numbers)))


print(eightyOne([4, 7]))
assert eightyOne([4, 7]) == "0b101"
assert eightyOne([11, 19]) == "0b1110"


def eightyTwo(data):
    """
    Write a Python program to find the sublist of numbers from a given list of numbers with only
    odd digits in increasing order.
    """

    def all_odd(number):
        return 0 not in map(lambda digit: digit == "-" or int(digit) % 2, str(number))

    def is_ascending(number):
        number = str(number)
        indexes = range(2 if number.startswith("-") else 1, len(number))
        filtered = filter(lambda i: int(number[i - 1]) < int(number[i]), indexes)
        return False not in filtered

    return sorted(filter(lambda number: all_odd(number) and is_ascending(number), data))


print(eightyTwo([-1, -3, -79, -10, -4, -2, -39]))
assert eightyTwo([1, 3, 79, 10, 4, 2, 39]) == [1, 3, 39, 79]
assert eightyTwo([11, 31, 40, 68, 77, 93, 48, 1, 57]) == [1, 11, 31, 57, 77, 93]
assert eightyTwo([9, -2, 3, 4, -2, 0, 2, -3, 8, -1]) == [-3, -1, 3, 9]
