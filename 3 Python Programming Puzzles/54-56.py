from math import log


def fiftyFour(data):
    """Write a Python program to remove duplicates from a list of integers, preserving order."""
    output = []
    for number in data:
        if number not in output:
            output.append(number)
    return output


def fiftyFive(data):
    """
    Write a Python program to find numbers that are greater than 10 and have odd first and last
    digits.
    """
    return [
        n for n in data if n > 10 and int(str(n)[0]) % 2 == int(str(n)[-1]) % 2 == 1
    ]


def fiftySix(a, n):
    """Write a Python program to find an integer exponent x such that a^x = n."""
    return round(log(n) / log(a))


print(fiftyFour([1, 3, 4, 10, 4, 1, 43]))
assert fiftyFour([1, 3, 4, 10, 4, 1, 43]) == [1, 3, 4, 10, 43]
assert fiftyFour([10, 11, 13, 23, 11, 25, 23, 76, 99]) == [10, 11, 13, 23, 25, 76, 99]

print(fiftyFive([1, 3, 79, 10, 4, 1, 39, 62]))
assert fiftyFive([1, 3, 79, 10, 4, 1, 39, 62]) == [79, 39]
assert fiftyFive([11, 31, 77, 93, 48, 1, 57]) == [11, 31, 77, 93, 57]

print(fiftySix(2, 1024))
assert fiftySix(2, 1024) == 10
assert fiftySix(3, 81) == 4
assert (
    fiftySix(
        3,
        1290070078170102666248196035845070394933441741644993085810116441344597492642263849,
    )
    == 170
)
