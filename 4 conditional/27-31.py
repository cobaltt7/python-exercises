def twentySeven():
    """Write a Python program to print the alphabet pattern 'T'."""
    out = ""

    for row in range(0, 7):
        for col in range(0, 5):
            out += "*" if row == 0 or col == 2 else " "

        out += "\n"

    return out


print(twentySeven())
assert twentySeven() == """*****
  * \u0020
  * \u0020
  * \u0020
  * \u0020
  * \u0020
  * \u0020
"""


def twentyEight():
    """Write a Python program to print the alphabet pattern 'U'."""
    out = ""

    for row in range(0, 7):
        for col in range(0, 5):
            out += "*" if (col in [0, 4]) ^ (row == 6) else " "

        out += "\n"

    return out


print(twentyEight())
assert twentyEight() == """*   *
*   *
*   *
*   *
*   *
*   *
 ***\u0020
"""


def twentyNine():
    """Write a Python program to print the alphabet pattern 'X'."""
    out = ""

    for row in range(0, 7):
        for col in range(0, 5):
            out += (
                "*"
                if (row in [0, 6] and col in [0, 4])
                or (row - 1 == col)
                or (row + col == 5)
                else " "
            )

        out += "\n"

    return out


print(twentyNine())
assert twentyNine() == """*   *
*   *
 * *\u0020
  * \u0020
 * *\u0020
*   *
*   *
"""


def thirty():
    """Write a Python program to print the alphabet pattern 'Z'."""
    out = ""

    for row in range(0, 7):
        for col in range(0, 7):
            out += "*" if row in [0, 6] or (row + col == 6) else " "

        out += "\n"

    return out


print(thirty())
assert thirty() == """*******
     *\u0020
    * \u0020
   *  \u0020
  *   \u0020
 *    \u0020
*******
"""


def thirtyOne(num):
    """
    Write a Python program to calculate a dog's age in dog years.

    Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog
    year equals 4 human years.
    """
    age = 0
    for year in range(num):
        age += 10.5 if year < 2 else 4
    return age


print(thirtyOne(15))
assert thirtyOne(0) == 0
assert thirtyOne(1) == 10.5
assert thirtyOne(2) == 21
assert thirtyOne(3) == 25
assert thirtyOne(4) == 29
assert thirtyOne(5) == 33
assert thirtyOne(15) == 73
