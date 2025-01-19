from math import floor


def eightyEight(even, odd):
    """
    Write a Python program to find an integer (n >= 0) with the given number of even and odd digits.
    """
    return int(("2" * even) + ("3" * odd))


print(eightyEight(2, 3))
assert eightyEight(2, 3) == 22333
assert eightyEight(4, 7) == 22223333333


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, floor(number / 2) + 1):
        if number % i == 0:
            return False
    return True


def eightyNine(data):
    """
    Write a Python program to find all integers <= 1000 that are the product of exactly three
    primes. Each integer should be represented as a list of its three prime factors.
    """

    output = []
    for one in range(data):
        if not is_prime(one):
            continue
        for two in range(data):
            if not is_prime(two):
                continue
            for three in range(data):
                if not is_prime(three):
                    continue
                if (one * two * three) > data:
                    continue
                output.append([one, two, three])
    return output


print(eightyNine(10))
assert eightyNine(10) == [[2, 2, 2]]
assert eightyNine(50) == [
    [2, 2, 2],
    [2, 2, 3],
    [2, 2, 5],
    [2, 2, 7],
    [2, 2, 11],
    [2, 3, 2],
    [2, 3, 3],
    [2, 3, 5],
    [2, 3, 7],
    [2, 5, 2],
    [2, 5, 3],
    [2, 5, 5],
    [2, 7, 2],
    [2, 7, 3],
    [2, 11, 2],
    [3, 2, 2],
    [3, 2, 3],
    [3, 2, 5],
    [3, 2, 7],
    [3, 3, 2],
    [3, 3, 3],
    [3, 3, 5],
    [3, 5, 2],
    [3, 5, 3],
    [3, 7, 2],
    [5, 2, 2],
    [5, 2, 3],
    [5, 2, 5],
    [5, 3, 2],
    [5, 3, 3],
    [5, 5, 2],
    [7, 2, 2],
    [7, 2, 3],
    [7, 3, 2],
    [11, 2, 2],
]


def ninety(data):
    """
    For each triple of eaten, need, and stock, write a Python program to get a pair of total
    appetite and remaining.
    """
    return [
        [eaten + min(need, stock), max(0, stock - need)] for eaten, need, stock in data
    ]


print(ninety([[2, 3, 18], [4, 9, 2], [2, 5, 7], [3, 8, 12], [4, 9, 106]]))
assert ninety([[2, 5, 6], [3, 9, 22]]) == [[7, 1], [12, 13]]
assert ninety([[2, 3, 18], [4, 9, 2], [2, 5, 7], [3, 8, 12], [4, 9, 106]]) == [
    [5, 15],
    [6, 0],
    [7, 2],
    [11, 4],
    [13, 97],
]
assert ninety([[1, 2, 3], [4, 5, 6]]) == [[3, 1], [9, 1]]
