def sixty_eight(string: str):
    """
    Write a Python program to create two strings from a given string. Create the first string using
    those character which occurs only once and create the second string which consists of multi-time
    occurring characters in the said string.
    """
    string = string.lower()
    unique = [
        character
        for character in string
        if string.index(character) == string.rindex(character)
    ]
    duplicates = [
        character
        for character in string
        if string.index(character) != string.rindex(character)
    ]
    duplicated = sorted(set(duplicates))
    return ("".join(sorted(unique)), "".join(duplicated))


print(sixty_eight("w3resource"))
assert sixty_eight("w3resource") == ("3cosuw", "er")
assert sixty_eight("aabbcceffgh") == ("egh", "abcf")


def sixty_nine(one: str, two: str):
    """Write a Python program to find the longest common sub-string from two given strings."""
    out = ""
    current = ""
    for char in one:
        updated = current + char
        if updated in two:
            current = updated
        else:
            if len(current) > len(out):
                out = current
            current = ""
    return out


print(sixty_nine("abcdefgh", "xswerabcdwd"))
assert sixty_nine("abcdefgh", "xswerabcdwd") == "abcd"
