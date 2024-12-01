def twentyFive():
    """Write a Python program to print the alphabet pattern 'R'."""
    out = ""

    for row in range(0, 7):
        for col in range(0, 5):
            out += (
                "*"
                if col == 0
                or (row == 4 and col == 2)
                or (row == 5 and col == 3)
                or row in ([1, 2, 6] if col == 4 else [0, 3])
                else " "
            )

        out += "\n"

    return out


print(twentyFive())
assert (
    twentyFive()
    == """****\u0020
*   *
*   *
****\u0020
* * \u0020
*  *\u0020
*   *
"""
)


def twentySix():
    """Write a Python program to print the following patterns."""

    def gen_s(fill="*"):
        count = len(fill)
        empty = " " * count

        out = ""
        for row in range(0, 7):
            line = ""
            for col in range(0, 5):
                line += (
                    fill
                    if (
                        (row in [1, 2, 6])
                        if (col == 0)
                        else (not row % 3) if (col in [1, 2, 3]) else (row in [0, 4, 5])
                    )
                    else empty
                )
            out += f"{line}\n" * count
        return out

    return [gen_s(), gen_s("ooo")]


print(twentySix()[0])
print(twentySix()[1])


def compare(actual, expected):
    for item_idx in range(len(actual)):
        actual_lines = actual[item_idx].split("\n")
        expected_lines = expected[item_idx].split("\n")
        for idx in range(len(actual_lines)):
            if actual_lines[idx] != expected_lines[idx]:
                raise AssertionError(
                    f"{item_idx}:{idx}: expected '{expected_lines[idx]}'; got"
                    f" '{actual_lines[idx]}'"
                )


compare(
    twentySix(),
    [
        """ ****
*   \u0020
*   \u0020
 ***\u0020
    *
    *
****\u0020
""",
        """   oooooooooooo
   oooooooooooo
   oooooooooooo
ooo           \u0020
ooo           \u0020
ooo           \u0020
ooo           \u0020
ooo           \u0020
ooo           \u0020
   ooooooooo  \u0020
   ooooooooo  \u0020
   ooooooooo  \u0020
            ooo
            ooo
            ooo
            ooo
            ooo
            ooo
oooooooooooo  \u0020
oooooooooooo  \u0020
oooooooooooo  \u0020
""",
    ],
)
