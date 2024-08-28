def sixteen(string, insert):
    """Write a Python function to insert a string in the middle of a string."""
    middle = int(len(string) / 2)
    return string[0:middle] + insert + string[middle:]


print(sixteen("[[]]", "Python"))
assert sixteen("[[]]", "Python") == "[[Python]]"
assert sixteen("{{}}", "PHP") == "{{PHP}}"
assert sixteen("<>", "HTML") == "<HTML>"


def seventeen(string):
    """
    Write a Python function to get a string made of 4 copies of the last two characters of a
    specified string (length must be at least 2).
    """
    return string[-2:] * 4


print(seventeen("Python"))
assert seventeen("Python") == "onononon"
assert seventeen("Exercises") == "eseseses"


def eightteen(string):
    """
    Write a Python function to get a string made of the first three characters of a specified
    string. If the length of the string is less than 3, return the original string.
    """
    return string[0:3]


print(eightteen("hi"))
assert eightteen("hi") == "hi"
assert eightteen("ipy") == "ipy"
assert eightteen("python") == "pyt"


def nineteen(string, character="/"):
    """Write a Python program to get the last part of a string before a specified character."""
    return string.split(character)[-1]


print(nineteen("https://www.w3resource.com/python-exercises"))
assert nineteen("https://www.w3resource.com/python-exercises") == "python-exercises"
assert nineteen("https://www.w3resource.com/python") == "python"
