from functools import reduce


def eTwentyFive(data):
    """Write a Python program to find the XOR of two given strings interpreted as binary numbers."""
    return reduce(
        lambda acc, number: acc ^ number, map(lambda number: int(number, 2), data), 0
    )


def eTwentySix(data):
    """
    Write a Python program to find the largest number where commas or periods are decimal
    points.
    """
    return reduce(
        lambda acc, number: acc if acc > number else number,  # type: ignore
        map(lambda number: float(number.replace(",", ".")), data),
        0,
    )


def eTwentySeven(data):
    """
    Squared deviations from the mean (SDM) are involved in various calculations. In probability
    theory and statistics, the definition of variance is either the expected value of the SDM (when
    considering a theoretical distribution) or its average value (for actual experimental data).
    Computations for analysis of variance involve the partitioning of a sum of SDM.

    Write a Python program to find x that minimizes the mean squared deviation from a given list of
    numbers.

    The problem requires minimizing the sum of squared deviations, which turns out to be the mean
    mu. Moreover, if mu is the mean of the numbers then a simple calculation.
    """
    return sum(data) / len(data)


assert eTwentyFive(["0001", "1011"]) == 0b1010
assert eTwentyFive(["100011101100001", "100101100101110"]) == 0b110001001111

assert eTwentySix(["100", "102,1", "101.1"]) == 102.1

assert eTwentySeven([4, -5, 17, -9, 14, 108, -9]) == 17.142857142857142
assert eTwentySeven([12, -2, 14, 3, -15, 10, -45, 3, 30]) == 1.1111111111111112
