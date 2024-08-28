def one_hundred(string: str):
    """
    Write a Python program to check whether any word in a given sting contains
    duplicate characrters or not. Return True or False.
    """
    return any(map(lambda word: len(set(word)) != len(word), string.split()))


print(one_hundred("Filter out the factorials of the said list."))
assert one_hundred("Filter out the factorials of the said list.") is True
assert one_hundred("Python Exercise.") is True
assert one_hundred("The wait is over.") is False


def one_hundred_one(one: str, two: str):
    """
    Write a Python program to add two strings as they are numbers (Positive integer
    values). Return a message if the numbers are string.
    """
    if one.isnumeric() and two.isnumeric():
        return int(one) + int(two)
    return "Invalid strings passed"


print(one_hundred_one("10", "22.6"))
assert one_hundred_one("10", "32") == 42
assert one_hundred_one("23", "43") == 66
assert one_hundred_one("10", "22.6") == "Invalid strings passed"
assert one_hundred_one("12", "11.6") == "Invalid strings passed"
assert one_hundred_one("100", "-200") == "Invalid strings passed"
assert one_hundred_one("200", "-100") == "Invalid strings passed"


def one_hundred_two(string: str):
    """Remove punctuations from a string."""
    return "".join(filter(lambda char: char == " " or char.isalnum(), string))


print(one_hundred_two("String! With. Punctuation?"))
assert one_hundred_two("String! With. Punctuation?") == "String With Punctuation"
assert one_hundred_two("@^&$String! With.-- Punctuation?") == "String With Punctuation"


def one_hundred_three(string: str, max_length: int):
    """Replace a word with hash characters in a string."""
    return " ".join(
        map(
            lambda word: "#" * len(word) if len(word) > max_length else word,
            string.split(" "),
        )
    )


print(one_hundred_three("Count the lowercase letters in the said list of words:", 4))
assert (
    one_hundred_three("Count the lowercase letters in the said list of words:", 4)
    == "##### the ######### ####### in the said list of ######"
)
assert (
    one_hundred_three("Python - Remove punctuations from a string:", 4)
    == "###### - ###### ############ from a #######"
)


def one_hundred_four(string: str):
    """Capitalize the first letter and lowercases the rest."""
    return " ".join(
        map(lambda word: word[0].upper() + word[1:].lower(), string.split(" "))
    )


print(one_hundred_four("Red Green WHITE"))
assert one_hundred_four("Red Green WHITE") == "Red Green White"
assert one_hundred_four("w3resource") == "W3resource"
assert (
    one_hundred_four("dow jones industrial average") == "Dow Jones Industrial Average"
)
