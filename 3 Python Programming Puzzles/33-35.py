from math import prod


def eThirtyThree(data):
    """
    Write a Python program to find the positions of all uppercase vowels (not counting Y) in even
    indices of a given string.
    """
    filtered = filter(
        lambda entry: (entry[0] % 2) == 0 and entry[1] in "AEIOU", enumerate(data)
    )
    return list(map(lambda entry: entry[0], filtered))


def eThirtyFour(data, k):
    """
    Write a Python program to find the sum of the numbers in a given list among the first k with
    more than 2 digits.
    """
    return sum(filter(lambda number: number > 99 or number < -99, data[:k]))


def eThirtyFive(data):
    """
    Write a Python program to compute the product of the odd digits in a given number, or 0 if
    there aren't any.
    """
    odd = list(map(int, filter(lambda digit: int(digit) % 2 == 1, str(data))))
    return prod(odd) if len(odd) else 0


assert eThirtyThree("w3rEsOUrcE") == [6]
assert eThirtyThree("AEIOUYW") == [0, 2, 4]

assert eThirtyFour([4, 5, 17, 9, 14, 108, -9, 12, 76], 4) == 0
assert eThirtyFour([4, 5, 17, 9, 14, 108, -9, 12, 76], 6) == 108
assert eThirtyFour([114, 215, -117, 119, 14, 108, -9, 12, 76], 5) == 331
assert eThirtyFour([114, 215, -117, 119, 14, 108, -9, 12, 76], 1) == 114

assert eThirtyFive(123456789) == 945
assert eThirtyFive(2468) == 0
assert eThirtyFive(13579) == 945
