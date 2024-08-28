def four():
    """Write a Python program to construct the following pattern, using a nested for loop."""
    output = ""
    for row in range(9):
        for column in range(row + 1 if row < 5 else 9 - row):
            output += "* "
        output += "\n"
    return output


print(four())
assert (
    four() == """* \n* * \n* * * \n* * * * \n* * * * * \n* * * * \n* * * \n* * \n* \n"""
)


def five(data, mode="F"):
    """Write a Python program that accepts a word from the user and reverses it."""
    return "".join(reversed(data))


print(five("Write a Python program that accepts a word from the user and reverses it."))
assert (
    five("Write a Python program that accepts a word from the user and reverses it.")
    == ".ti sesrever dna resu eht morf drow a stpecca taht margorp nohtyP a etirW"
)


def six(data):
    """
    Write a Python program to count the number of even and odd numbers in a series of numbers
    """
    even = len(list(filter(lambda number: number % 2, data)))
    return (even, len(data) - even)


print(six((1, 2, 3, 4, 5, 6, 7, 8, 9)))
assert six((1, 2, 3, 4, 5, 6, 7, 8, 9)) == (5, 4)
