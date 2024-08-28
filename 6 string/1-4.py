def one(numbers):
    """Write a Python program to calculate the length of a string."""
    return len(numbers)


print(one("w3resource.com"))
assert one("w3resource.com") == 14


def two(string):
    """
    Write a Python program to count the number of characters (character frequency) in a string.
    """
    counts = {}
    for character in string:
        if character not in counts:
            counts[character] = 0
        counts[character] = counts[character] + 1
    return counts


print(two("google.com"))
assert two("google.com") == {"g": 2, "o": 3, "l": 1, "e": 1, ".": 1, "c": 1, "m": 1}


def three(string):
    """
    Write a Python program to get a string made of the first 2 and last 2 characters of a given
    string. If the string length is less than 2, return the empty string instead.
    """
    return "" if len(string) < 2 else string[:2] + string[-2:]


print(three("w3resource"))
assert three("w3resource") == "w3ce"
assert three("w3") == "w3w3"
assert three("w") == ""


def four(string):
    """
    Write a Python program to get a string from a given string where all occurrences of its first
    char have been changed to '$', except the first char itself.
    """
    return string[0] + string[1:].replace(string[0], "$")


print(four("restartr"))
assert four("restart") == "resta$t"
