from functools import reduce


def fourty(number):
    """Write a Python program to reverse words in a string."""
    return " ".join(number.split()[::-1])


print(fourty("The quick brown fox jumps over the lazy dog."))
assert (
    fourty("The quick brown fox jumps over the lazy dog.")
    == "dog. lazy the over jumps fox brown quick The"
)
assert fourty("Python Exercises.") == "Exercises. Python"


def fourty_two(string, characters):
    """Write a Python program to strip a set of characters from a string."""
    return reduce(lambda string, char: string.replace(char, ""), characters, string)


print(fourty_two("The quick brown fox jumps over the lazy dog.", "aeiou"))
assert (
    fourty_two("The quick brown fox jumps over the lazy dog.", "aeiou")
    == "Th qck brwn fx jmps vr th lzy dg."
)


def fourty_three(string):
    """Write apython program to count repeated characters in a string."""
    counts = {}
    for character in string:
        if character not in counts:
            counts[character] = 0
        counts[character] = counts[character] + 1
    return {character: count for character, count in counts.items() if count > 1}


print(fourty_three("thequickbrownfoxjumpsoverthelazydog"))
assert fourty_three("thequickbrownfoxjumpsoverthelazydog") == {
    "o": 4,
    "e": 3,
    "h": 2,
    "t": 2,
    "r": 2,
    "u": 2,
}
