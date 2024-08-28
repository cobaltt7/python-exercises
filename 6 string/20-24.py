def twenty(string):
    """Write a Python function to reverse a string if its length is a multiple of 4."""
    return string if len(string) % 4 else string[::-1]


print(twenty("abcd"))
assert twenty("abcd") == "dcba"
assert twenty("python") == "python"
assert twenty("html&php") == "php&lmth"


def twenty_one(string):
    """
    Write a Python function to convert a given string to all uppercase if it contains at least 2
    uppercase characters in the first 4 characters.
    """
    upper = 0
    for char in string[:4]:
        if char.isupper():
            upper += 1
        if upper >= 2:
            break
    return string.upper() if upper >= 2 else string


print(twenty_one("Python"))
assert twenty_one("Python") == "Python"
assert twenty_one("PyThon") == "PYTHON"


def twenty_two(string):
    """Write a Python program to sort a string lexicographically."""
    return sorted(string, key=lambda char: char.upper())


print(twenty_two("w3resource"))
assert twenty_two("w3resource") == ["3", "c", "e", "e", "o", "r", "r", "s", "u", "w"]
assert twenty_two("quickbrown") == ["b", "c", "i", "k", "n", "o", "q", "r", "u", "w"]


def twenty_three(string):
    """Write a Python program to remove a newline in Python."""
    return string.replace("\n", "")


print(twenty_three("Python Exercises\n"))
assert twenty_three("Python Exercises\n") == "Python Exercises"


def twenty_four(string, characters):
    """Write a Python program to check whether a string starts with specified characters."""
    return string.startswith(characters)


print(twenty_four("w3resource.com", "w3r"))
assert twenty_four("w3resource.com", "w3r") is True
