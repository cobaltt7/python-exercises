def thirty_six(number):
    """Write a Python program to format a number with a percentage."""
    return f"{number:.2%}"


print(thirty_six(0.25))
assert thirty_six(0.25) == "25.00%"
assert thirty_six(-0.25) == "-25.00%"


def thirty_seven(number):
    """
    Write a Python program to display a number in left, right, and center aligned with a width of
    10.
    """
    number = str(number)
    return [number.ljust(10, " "), number.rjust(10, " "), number.center(10, " ")]


print(thirty_seven(22))
assert thirty_seven(22) == ["22        ", "        22", "    22    "]


def thirty_eight(string, substring):
    """Write a Python program to count occurrences of a substring in a string."""
    return string.count(substring)


print(thirty_eight("The quick brown fox jumps over the lazy dog.", "fox"))
assert thirty_eight("The quick brown fox jumps over the lazy dog.", "fox") == 1


def thirty_nine(string):
    """Write a Python program to reverse a string."""
    return string[::-1]


print(thirty_nine("abcdef"))
assert thirty_nine("abcdef") == "fedcba"
assert thirty_nine("Python Exercises.") == ".sesicrexE nohtyP"
