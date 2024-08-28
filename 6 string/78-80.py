def seventy_eight(string: str):
    """
    Write a Python program to count characters at the same position in a given string
    (lower and uppercase characters) as in the English alphabet.
    """
    a = ord("a")
    count = 0
    for index, character in enumerate(string.lower()):
        if (ord(character) - a) == index:
            count += 1
    return count


print(seventy_eight("xbcefg"))
assert seventy_eight("xbcefg") == 2


def seventy_nine(string: str):
    """Write a Python program to find smallest and largest word in a given string."""
    short = None
    long = None
    for word in string.split():
        if not short or len(word) < len(short):
            short = word
        if not long or len(word) > len(long):
            long = word
    return (short, long)


print(seventy_nine("A quick red fox"))
assert seventy_nine("A quick red fox") == ("A", "quick")
assert seventy_nine(
    " Write a Java program to sort an array of given integers using Quick sort"
    " Algorithm."
) == ("a", "Algorithm.")


def eighty(string: str):
    """
    Write a Python program to count number of substrings with same first and last
    characters of a given string.
    """
    count = 0
    length = len(string)
    for start in range(length):
        for end in range(start, length):
            if string[start] == string[end]:
                count += 1
    return count


print(eighty("abc"))
assert eighty("abc") == 3
