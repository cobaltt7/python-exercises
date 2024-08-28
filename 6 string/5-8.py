def five(string):
    """
    Write a Python program to get a single string from two given strings, separated by a space and
    swap the first two characters of each string.
    """
    words = string.split()
    return f"{words[1][0:2]}{words[0][2:]} {words[0][0:2]}{words[1][2:]}"


print(five("abc xyz"))
assert five("abc xyz") == "xyc abz"


def six(string):
    """
    Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
    If the given string already ends with 'ing', add 'ly' instead. If the string length of the
    given string is less than 3, leave it unchanged.
    """
    return (
        string
        if len(string) < 3
        else string + ("ly" if string.endswith("ing") else "ing")
    )


print(six("abc"))
assert six("abc") == "abcing"
assert six("string") == "stringly"


def seven(string):
    """
    Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a
    given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'.
    Return the resulting string.
    """
    if ("not" not in string) or ("poor" not in string):
        return string

    not_index = string.index("not")
    poor_index = string.index("poor")
    if not_index > poor_index:
        return string

    return string[0:not_index] + "good" + string[poor_index + 4 :]


print(seven("The lyrics is not that poor!"))
assert seven("The lyrics is not that poor!") == "The lyrics is good!"
assert seven("The lyrics is poor!") == "The lyrics is poor!"


def eight(string):
    """
    Write a Python function that takes a list of words and return the longest word and the length
    of the longest one.
    """
    return sorted(string.split(), key=len, reverse=True)[0]


print(eight("PHP Exercises Backend"))
assert eight("PHP Exercises Backend") == "Exercises"
