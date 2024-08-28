def nineteen():
    """Write a Python program to print the alphabet pattern 'E'."""
    out = ""

    for row in range(0, 7):
        for col in range(0, 5):
            out += (
                "*" if (col == 0) or (row in [0, 6]) or (row == 3 and col < 4) else " "
            )

        out += "\n"

    return out


print(nineteen())
assert nineteen() == """*****
*   \u0020
*   \u0020
****\u0020
*   \u0020
*   \u0020
*****
"""


def twenty():
    """Write a Python program to print the alphabet pattern 'G'."""
    out = ""

    for row in range(0, 7):
        for col in range(0, 5):
            out += (
                "*"
                if (0 < col < 4 if row in [0, 6] else col == 0)
                or (row in [1, 3, 4, 5] and col == 4)
                or (row == 3 and col > 1)
                else " "
            )

        out += "\n"

    return out


print(twenty())
assert twenty() == """ ***\u0020
*   *
*   \u0020
* ***
*   *
*   *
 ***\u0020
"""


def twentyOne():
    """Write a Python program to print the alphabet pattern 'L'."""
    out = ""

    for row in range(0, 7):
        for col in range(0, 5):
            out += "*" if col == 0 or row == 6 else " "

        out += "\n"

    return out


print(twentyOne())
assert twentyOne() == """*   \u0020
*   \u0020
*   \u0020
*   \u0020
*   \u0020
*   \u0020
*****
"""
