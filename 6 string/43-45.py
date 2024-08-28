def fourty():
    """
    Write a Python program to print the square and cube symbol in the area of a rectangle and
    volume of a cylinder.
    """
    return (f"{1256.66:.1f}cm\u00b2", f"{1254.725:.1f}cm\u00b3")


print(fourty())
assert fourty() == ("1256.7cm²", "1254.7cm³")


def fourty_two(string):
    """Write a Python program to print the index of the character in a string."""
    return list(enumerate(string))


print(fourty_two("The quick brown fox jumps over the lazy dog."))
assert fourty_two("The quick brown fox jumps over the lazy dog.") == [
    (0, "T"),
    (1, "h"),
    (2, "e"),
    (3, " "),
    (4, "q"),
    (5, "u"),
    (6, "i"),
    (7, "c"),
    (8, "k"),
    (9, " "),
    (10, "b"),
    (11, "r"),
    (12, "o"),
    (13, "w"),
    (14, "n"),
    (15, " "),
    (16, "f"),
    (17, "o"),
    (18, "x"),
    (19, " "),
    (20, "j"),
    (21, "u"),
    (22, "m"),
    (23, "p"),
    (24, "s"),
    (25, " "),
    (26, "o"),
    (27, "v"),
    (28, "e"),
    (29, "r"),
    (30, " "),
    (31, "t"),
    (32, "h"),
    (33, "e"),
    (34, " "),
    (35, "l"),
    (36, "a"),
    (37, "z"),
    (38, "y"),
    (39, " "),
    (40, "d"),
    (41, "o"),
    (42, "g"),
    (43, "."),
]


def fourty_three(string):
    """Write a Python program to check if a string contains all letters of the alphabet."""
    letters = "".join(sorted(set(string.lower())))
    return "abcdefghijklmnopqrstuvwxyz" in letters


print(fourty_three("The quick brown fox jumps over the lazy dog."))
assert fourty_three("The quick brown fox jumps over the lazy dog.") is True
assert fourty_three("The quick brown fox jumps over the lazy cat.") is False
