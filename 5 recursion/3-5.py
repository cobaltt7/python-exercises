def three(numbers):
    """Write a Python program to sum recursion lists."""
    if not len(numbers):
        return 0
    first = three(numbers[0]) if isinstance(numbers[0], list) else numbers[0]
    return first + three(numbers[1:])


print(three([1, 2, [3, 4], [5, 6]]))
assert three([1, 2, [3, 4], [5, 6]]) == 21


def four(number):
    """Write a Python program to get the factorial of a non-negative integer."""
    if number == 1:
        return 1
    return number * four(number - 1)


print(four(5))
assert four(5) == 120


def five(index):
    """Write a Python program to solve the Fibonacci sequence using recursion."""
    if index == 0:
        return [0]
    previous = five(index - 1)
    return [*previous, 1 if index == 1 else sum(previous[-2:])]


print(five(19))
assert five(19) == [
    0,
    1,
    1,
    2,
    3,
    5,
    8,
    13,
    21,
    34,
    55,
    89,
    144,
    233,
    377,
    610,
    987,
    1597,
    2584,
    4181,
]
