def thirtyTwo(letter):
    """Write a Python program to check whether an alphabet is a vowel or consonant."""
    return (
        "vowel"
        if letter in "aeiouyAEIOU"
        else ("consonant" if letter.isalpha() else "symbol")
    )


print(thirtyTwo("k"))
assert thirtyTwo("k") == "consonant"
assert thirtyTwo("a") == "vowel"
assert thirtyTwo(".") == "symbol"


def thirtyThree(month):
    """
    Write a Python program to convert a month name to a number of days.

    List of months: January, February, March, April, May, June, July, August, September, October,
    November, December
    """
    return (
        30
        if month in ["September", "April", "June", "November"]
        else (28.25 if month == "February" else 31)
    )


print(thirtyThree("February"))
assert thirtyThree("February") == 28.25
assert thirtyThree("June") == 30
assert thirtyThree("October") == 31


def thirtyFour(num1, num2):
    """Write a Python program to sum two integers. However, if the sum is between 15 and 20 it will
    return 20."""
    sum = num1 + num2
    return 20 if 15 < sum < 20 else sum


print(thirtyFour(1, 2))
assert thirtyFour(1, 2) == 3
assert thirtyFour(10, 20) == 30
assert thirtyFour(11, 5) == 20


def thirtyFive(string):
    """Write a Python program that checks whether a string represents an integer or not."""
    return string.isnumeric()


print(thirtyFive("Python"))
assert thirtyFive("Python") is False
assert thirtyFive("130") is True


def thirtySix(x, y, z):
    """
    Write a Python program to check if a triangle is equilateral, isosceles or scalene.

    Note:
    - An equilateral triangle is a triangle in which all three sides are equal.
    - A scalene triangle is a triangle that has three unequal sides.
    - An isosceles triangle is a triangle with (at least) two equal sides.
    """
    unique = len(set([x, y, z]))
    return ["Equilateral", "Isosceles", "Scalene"][unique - 1]


print(thirtySix(4, 4, 6))
assert thirtySix(6, 8, 12) == "Scalene"
assert thirtySix(5, 5, 5) == "Equilateral"
assert thirtySix(4, 4, 6) == "Isosceles"
