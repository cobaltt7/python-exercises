from typing import Any


def thirty_two(data: list[Any], subset: list[Any]):
    """Write a Python program to check whether a list contains a sublist."""
    index = 0
    for item in data:
        if index == len(subset):
            return True
        if item == subset[index]:
            index += 1
        else:
            index = 0
    return False


print(thirty_two([2, 4, 3, 5, 7], [4, 3]))
assert thirty_two([2, 4, 3, 5, 7], [4, 3]) is True
assert thirty_two([2, 4, 3, 5, 7], [3, 7]) is False


def thirty_three(data: list[Any]):
    """Write a Python program to generate all sublists of a list."""
    output = []
    for index in range(len(data)):
        for subindex in range(index + 1):
            output.append(data[subindex : index + 1])
    return output


print(thirty_three([10, 20, 30, 40]))
assert thirty_three(["x", "y", "z"]) == [
    ["x"],
    ["x", "y"],
    ["y"],
    ["x", "y", "z"],
    ["y", "z"],
    ["z"],
]
assert thirty_three([10, 20, 30, 40]) == [
    [10],
    [10, 20],
    [20],
    [10, 20, 30],
    [20, 30],
    [30],
    [10, 20, 30, 40],
    [20, 30, 40],
    [30, 40],
    [40],
]


def thirty_four(number: int):
    """
    Write a Python program that uses the Sieve of Eratosthenes method to compute prime numbers up to
    a specified number.

    Note: In mathematics, the sieve of Eratosthenes, (Ancient Greek: κόσκινον Ἐρατοσθένους, kóskinon
    Eratosthénous) one of a number of prime number sieves, is a simple, ancient algorithm for
    finding all prime numbers up to any given limit.
    """
    seen = []
    primes = []
    numbers = range(2, number + 1)

    def get_p():
        for number in numbers:
            if number not in seen:
                return number
        return None

    while p := get_p():
        current = p
        primes.append(p)
        index = 1
        while current <= number:
            seen.append(current)
            index += 1
            current = p * index
    return primes


print(thirty_four(100))
assert thirty_four(100) == [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
]
assert thirty_four(10) == [2, 3, 5, 7]
assert thirty_four(11) == [2, 3, 5, 7, 11]
