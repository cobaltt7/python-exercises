def sixteen():
    """
    Write a Python program to find numbers between 100 and 400 (both included) where each digit of
    a number is an even number. The numbers obtained should be printed in a comma-separated
    sequence.
    """
    out = []
    for number in range(100, 401):
        digits = str(number)
        qualifies = True
        for digit in digits:
            if int(digit) % 2 == 1:
                qualifies = False
                break
        if qualifies:
            out.append(number)
    return out


print(sixteen())


def seventeen():
    """Write a Python program to print the alphabet pattern 'D'."""
    out = ""

    for row in range(0, 7):
        for col in range(0, 5):
            out += (
                "*"
                if (0 < col < 4 and row == 0)
                or (col in [0, 4] and row > 0)
                or (row == 3)
                else " "
            )

        out += "\n"

    return out


print(seventeen())
assert (
    seventeen()
    == """ ***\u0020
*   *
*   *
*****
*   *
*   *
*   *
"""
)


def eighteen():
    """Write a Python program to print the alphabet pattern 'D'."""
    out = ""

    for row in range(0, 7):
        for col in range(0, 5):
            out += (
                "*"
                if (row in [0, 6] and col < 4)
                or (col == 0)
                or (0 < row < 6 and col == 4)
                else " "
            )

        out += "\n"

    return out


print(eighteen())
assert (
    eighteen()
    == """****\u0020
*   *
*   *
*   *
*   *
*   *
****\u0020
"""
)
