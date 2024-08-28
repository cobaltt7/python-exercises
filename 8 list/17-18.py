from typing import Any
from math import floor


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, floor(number / 2) + 1):
        if number % i == 0:
            return False
    return True


def seventeen(data: list[int]):
    """
    Write a Python program to check if each number is prime in a given list of numbers. Return True
    if all numbers are prime otherwise False.
    """
    return all(is_prime(number) for number in data)


print(seventeen([0, 3, 4, 7, 9]))
assert seventeen([0, 3, 4, 7, 9]) is False
assert seventeen([3, 5, 7, 13]) is True
assert seventeen([1, 5, 3]) is False


def eighteen(data: list[Any]):
    """
    Write a Python program to generate all permutations of a list in Python.

    In mathematics, the notion of permutation relates to the act of arranging all the members of a
    set into some sequence or order, or if the set is already ordered, rearranging (reordering) its
    elements, a process called permuting. These differ from combinations, which are selections of
    some members of a set where order is disregarded.

    In the following image each of the six rows is a different permutation of three distinct balls.
    """
    if len(data) == 0:
        return [[]]

    output = []

    for index, number in enumerate(data):
        for perm in eighteen(data[:index] + data[index+1:]):
            output.append((number, *perm))

    return output


print(eighteen([1, 2, 3]))
assert eighteen([1, 2, 3]) == [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
