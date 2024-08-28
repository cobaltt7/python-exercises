from difflib import SequenceMatcher


def ninety(string: str):
    """Write a Python program to remove duplicate words from a given string."""
    return " ".join(dict.fromkeys(string.split()))


print(ninety("Python Exercises Practice Solution Exercises"))
assert (
    ninety("Python Exercises Practice Solution Exercises")
    == "Python Exercises Practice Solution"
)


def ninety_one(scalars: list):
    """
    Write a Python program to convert a given heterogeneous list of scalars into a
    string.
    """
    return ",".join(str(scalar) for scalar in scalars)


print(ninety_one(["Red", 100, -50, "green", "w,3,r", 12.12, False]))
assert (
    ninety_one(["Red", 100, -50, "green", "w,3,r", 12.12, False])
    == "Red,100,-50,green,w,3,r,12.12,False"
)


def ninety_two(one: str, two: str):
    """
    Write a Python program to find the string similarity between two given strings.
    """
    return SequenceMatcher(None, one, two).ratio()


print(ninety_two("Python Exercises", "Python Exercises"))
assert ninety_two("Python Exercises", "Python Exercises") == 1.0
assert ninety_two("Python Exercises", "Python Exercise") == 0.967741935483871
assert ninety_two("Python Exercises", "Python Ex.") == 0.6923076923076923
assert ninety_two("Python Exercises", "Python") == 0.5454545454545454
assert ninety_two("Java Exercises", "Python") == 0.0


def ninety_three(string: str):
    """Write a Python program to extract numbers from a given string."""
    return [float(found) for found in string.split() if found.isnumeric()]


print(ninety_three("red 12 black 45 green"))
assert ninety_three("red 12 black 45 green") == [12, 45]


def ninety_four(color: str):
    """
    Write a Python program to convert a hexadecimal color code to a tuple of integers
    corresponding to its RGB components.
    """
    if color[0] == "#":
        color = color[1:]
    if len(color) < 6:
        color = color[0] + color[0:2] + color[1:3] + color[2]
    return (int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16))


print(ninety_four("FFA501"))
assert ninety_four("FFA501") == (255, 165, 1)
assert ninety_four("FFFFFF") == (255, 255, 255)
assert ninety_four("000000") == (0, 0, 0)
assert ninety_four("FF0000") == (255, 0, 0)
assert ninety_four("000080") == (0, 0, 128)
assert ninety_four("C0C0C0") == (192, 192, 192)
assert ninety_four("#FFA501") == (255, 165, 1)
assert ninety_four("FFF") == (255, 255, 255)
assert ninety_four("#FFF") == (255, 255, 255)
