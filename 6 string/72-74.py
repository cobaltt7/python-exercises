def seventy_two(string: str, search: str):
    """
    Write a Python program to remove all characters except a specified character from a given
    string.
    """
    return "".join(char for char in string if char == search)


print(seventy_two("Python Exercises", "P"))
assert seventy_two("Python Exercises", "P") == "P"
assert seventy_two("google", "g") == "gg"
assert seventy_two("exercises", "e") == "eee"


def seventy_three(string: str):
    """
    Write a Python program to count Uppercase, Lowercase, special character and numeric values in a
    given string.
    """
    upper = 0
    lower = 0
    special = 0
    number = 0
    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isnumeric():
            number += 1
        else:
            special += 1
    return (upper, lower, special, number)


print(seventy_three("@W3Resource,Com"))
assert seventy_three("@W3Resource,Com") == (3, 9, 2, 1)


def seventy_four(string: str, contained: str):
    """
    Write a Python program to find the minimum window in a given string which will contain all the
    characters of another given string.
    """
    out = string
    while all(map(lambda char: char in out[1:], contained)):
        out = out[1:]
    while all(map(lambda char: char in out[:-1], contained)):
        out = out[:-1]
    return out


print(seventy_four("PRWSOERIUSFK", "OSU"))
assert seventy_four("PRWSOERIUSFK", "OSU") == "OERIUS"
