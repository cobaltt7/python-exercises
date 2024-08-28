def twelve(string):
    """Write a Python program to count the occurrences of each word in a given sentence."""
    counts = {}
    for character in string.split():
        if character not in counts:
            counts[character] = 0
        counts[character] = counts[character] + 1
    return counts


print(twelve("the quick brown fox jumps over the lazy dog."))
assert twelve("the quick brown fox jumps over the lazy dog.") == {
    "the": 2,
    "jumps": 1,
    "brown": 1,
    "lazy": 1,
    "fox": 1,
    "over": 1,
    "quick": 1,
    "dog.": 1,
}


def thirteen(string):
    """
    Write a Python script that takes input from the user and displays that input back in upper
    and lower cases.
    """
    return (string.upper(), string.lower())


print(thirteen("English"))
assert thirteen("English") == ("ENGLISH", "english")


def fourteen(string):
    """
    Write a Python program that accepts a comma-separated sequence of words as input and prints
    the distinct words in sorted form (alphanumerically).
    """
    return ",".join(sorted(set(string.split(","))))


print(fourteen("red,white,black,red,green,black"))
assert fourteen("red,white,black,red,green,black") == "black,green,red,white"


def fifteen(tag, string):
    """Write a Python function to create an HTML string with tags around the word(s)."""
    return f"<{tag}>{string}</{tag}>"


print(fifteen("i", "Python"))
assert fifteen("i", "Python") == "<i>Python</i>"
assert fifteen("b", "Python Tutorial") == "<b>Python Tutorial</b>"
