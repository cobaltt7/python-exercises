from typing import Any


def two_six_one(data: list[float]):
    """
    Write a Python program to get the most frequent element in a given list of numbers.
    """
    frequencies: dict[float, int] = {}
    for item in data:
        if item in frequencies:
            frequencies[item] += 1
        else:
            frequencies[item] = 1
    return sorted(frequencies.items(), key=lambda item: item[1], reverse=True)[0][0]


print(two_six_one([2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]))
assert two_six_one([2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]) == 2
assert two_six_one([1, 2, 3, 1, 2, 3, 2, 1, 4, 3, 3]) == 3


def two_six_two(data: list[Any], count: int):
    """
    Write a Python program to move the specified number of elements to the end of the
    given list.
    """
    return data[count:] + data[:count]


print(two_six_two([1, 2, 3, 4, 5, 6, 7, 8], 3))
assert two_six_two([1, 2, 3, 4, 5, 6, 7, 8], 3) == [4, 5, 6, 7, 8, 1, 2, 3]
assert two_six_two([1, 2, 3, 4, 5, 6, 7, 8], -3) == [6, 7, 8, 1, 2, 3, 4, 5]
assert two_six_two([1, 2, 3, 4, 5, 6, 7, 8], 1) == [2, 3, 4, 5, 6, 7, 8, 1]
assert two_six_two([1, 2, 3, 4, 5, 6, 7, 8], -7) == [2, 3, 4, 5, 6, 7, 8, 1]
assert two_six_two([1, 2, 3, 4, 5, 6, 7, 8], 7) == [8, 1, 2, 3, 4, 5, 6, 7]
assert two_six_two([1, 2, 3, 4, 5, 6, 7, 8], -1) == [8, 1, 2, 3, 4, 5, 6, 7]
assert two_six_two([1, 2, 3, 4, 5, 6, 7, 8], 8) == [1, 2, 3, 4, 5, 6, 7, 8]
assert two_six_two([1, 2, 3, 4, 5, 6, 7, 8], -8) == [1, 2, 3, 4, 5, 6, 7, 8]


def two_six_three(data: list[Any], count: int):
    """
    Write a Python program to move the specified number of elements to the start of the
    given list.
    """
    return data[-count:] + data[:-count]


print(two_six_three([1, 2, 3, 4, 5, 6, 7, 8], 3))
assert two_six_three([1, 2, 3, 4, 5, 6, 7, 8], 3) == [6, 7, 8, 1, 2, 3, 4, 5]
assert two_six_three([1, 2, 3, 4, 5, 6, 7, 8], -3) == [4, 5, 6, 7, 8, 1, 2, 3]
assert two_six_three([1, 2, 3, 4, 5, 6, 7, 8], 7) == [2, 3, 4, 5, 6, 7, 8, 1]
assert two_six_three([1, 2, 3, 4, 5, 6, 7, 8], -7) == [8, 1, 2, 3, 4, 5, 6, 7]
assert two_six_three([1, 2, 3, 4, 5, 6, 7, 8], 8) == [1, 2, 3, 4, 5, 6, 7, 8]
assert two_six_three([1, 2, 3, 4, 5, 6, 7, 8], -8) == [1, 2, 3, 4, 5, 6, 7, 8]


def two_six_four(data: list[list[Any]]):
    """
    Write a Python program to create a two-dimensional list from a given list of lists.
    """
    length = len(sorted(data, key=len, reverse=True)[0])
    output: list[list[Any]] = []
    for i in range(length):
        output.append([])
        for sublist in data:
            output[-1].append(sublist[i])
    return output


print(two_six_four([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))
assert two_six_four([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]) == [
    [1, 4, 7, 10],
    [2, 5, 8, 11],
    [3, 6, 9, 12],
]
assert two_six_four([[1, 2], [4, 5]]) == [[1, 4], [2, 5]]


def two_six_five(count: int):
    """
    Write a Python program to generate a list containing the Fibonacci sequence, up
    until the nth term.
    """
    prev_num = 0
    next_num = 1
    output: list[int] = [0]
    while len(output) <= count:
        output.append(next_num)
        next_num = next_num + prev_num
        prev_num = output[-1]
    return output


print(two_six_five(7))
assert two_six_five(7) == [0, 1, 1, 2, 3, 5, 8, 13]
assert two_six_five(15) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
assert two_six_five(50) == [
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
    6765,
    10946,
    17711,
    28657,
    46368,
    75025,
    121393,
    196418,
    317811,
    514229,
    832040,
    1346269,
    2178309,
    3524578,
    5702887,
    9227465,
    14930352,
    24157817,
    39088169,
    63245986,
    102334155,
    165580141,
    267914296,
    433494437,
    701408733,
    1134903170,
    1836311903,
    2971215073,
    4807526976,
    7778742049,
    12586269025,
]
