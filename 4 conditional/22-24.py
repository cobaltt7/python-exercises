def twentyTwo():
    """Write a Python program to print the alphabet pattern 'M'."""
    out = ""

    for row in range(0, 7):
        for col in range(0, 9):
            out += (
                "*"
                if (col in [0, 8])
                or (col in [2, 6] and row == 2)
                or (col == 4 and row == 3)
                else " "
            )

        out += "\n"

    return out


print(twentyTwo())
assert (
    twentyTwo()
    == """*       *
*       *
* *   * *
*   *   *
*       *
*       *
*       *
"""
)


def twentyThree():
    """Write a Python program to print the alphabet pattern 'O'."""
    out = ""

    for row in range(0, 7):
        for col in range(0, 5):
            out += "*" if (col in [0, 4]) ^ (row in [0, 6]) else " "

        out += "\n"

    return out


print(twentyThree())
assert (
    twentyThree()
    == """ ***\u0020
*   *
*   *
*   *
*   *
*   *
 ***\u0020
"""
)


def twentyFour():
    """Write a Python program to print the alphabet pattern 'P'."""
    out = ""

    for row in range(0, 7):
        for col in range(0, 5):
            out += (
                "*" if col == 0 or (0 < row < 3 if col == 4 else row in [0, 3]) else " "
            )

        out += "\n"

    return out


print(twentyFour())
assert (
    twentyFour()
    == """****\u0020
*   *
*   *
****\u0020
*   \u0020
*   \u0020
*   \u0020
"""
)
