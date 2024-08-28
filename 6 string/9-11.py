def nine(string, number):
    """Write a Python program to remove the n^th index character from a nonempty string."""
    return string[:number] + string[number + 1 :]


print(nine("Python", 0))
assert nine("Python", 0) == "ython"
assert nine("Python", 3) == "Pyton"
assert nine("Python", 5) == "Pytho"


def ten(string):
    """
    Write a Python program to change a given string to a newly string where the first and last
    chars have been exchanged.
    """
    return string[-1] + string[1:-1] + string[0]


print(ten("abcd"))
assert ten("abcd") == "dbca"
assert ten("12345") == "52341"


def eleven(string):
    """Write a Python program to remove characters that have odd index values in a given string."""
    return string[::2]


print(eleven("abcdef"))
assert eleven("abcdef") == "ace"
assert eleven("python") == "pto"
