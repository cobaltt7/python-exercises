from math import sqrt
import datetime


def fourty(one, two, three):
    """Write a Python program to find the median of three values."""
    return sorted([one, two, three])[1]


print(fourty(15, 26, 29))
assert fourty(15, 26, 29) == 26


def fourtyOne(year, month, date):
    """Write a Python program to get the next day of a given date."""
    return (datetime.date(year, month, date) + datetime.timedelta(1)).strftime(
        "%Y-%m-%d"
    )


print(fourtyOne(2026, 8, 23))
assert fourtyOne(2026, 8, 23) == "2026-08-24"


def thirtyNine():
    """
    Write a Python program to calculate the sum and average of n integer numbers (input from the
    user). Input 0 to finish.
    """
    numbers = []
    number = int(input("number"))
    while number:
        numbers.append(number)
        number = int(input("number"))
    summed = sum(numbers)
    return (summed, summed / len(numbers))


print(thirtyNine())


def euclidean_distance(p, q):
    sum = 0

    n = len(p)
    for k in range(n):
        sum += (p[k] - q[k]) ** 2

    dist = sqrt(sum)
    return dist
