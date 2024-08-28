def fourty_six(string):
    """Write a Python program to convert a given string into a list of words."""
    return string.split()


print(fourty_six("The quick brown fox jumps over the lazy dog."))
assert fourty_six("The quick brown fox jumps over the lazy dog.") == [
    "The",
    "quick",
    "brown",
    "fox",
    "jumps",
    "over",
    "the",
    "lazy",
    "dog.",
]


def fourty_seven(string, n):
    """Write a Python program to convert a given string into a list of words."""
    return string[:n].lower() + string[n:]


print(fourty_seven("W3RESOURCE.COM", 4))
assert fourty_seven("W3RESOURCE.COM", 4) == "w3reSOURCE.COM"


def fourty_eight(string):
    """Write a Python program to swap comma and dot in a string."""
    return ".".join(map(lambda segment: segment.replace(".", ","), string.split(",")))


print(fourty_eight("32.054,23"))
assert fourty_eight("32.054,23") == "32,054.23"


def fourty_nine(string):
    """Write a Python program to count and display the vowels of a given text."""
    vowels = [letter for letter in string.lower() if letter in "aeiouy"]
    return (len(vowels), set(vowels))


print(fourty_nine("w3resource.com"))
assert fourty_nine("w3resource.com") == (5, {"o", "u", "e"})
