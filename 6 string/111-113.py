def one_hundred_eleven(string: str):
    """
    Write a Python program that takes a string and replaces all the characters with their respective
    numbers.
    """
    return " ".join(
        str(ord(character) - 64) for character in string.upper() if character.isalpha()
    )


print(one_hundred_eleven("Python Tutorial"))
assert one_hundred_eleven("Aa") == "1 1"
assert one_hundred_eleven("Python") == "16 25 20 8 15 14"
assert one_hundred_eleven("Java") == "10 1 22 1"
assert one_hundred_eleven("Python Tutorial") == "16 25 20 8 15 14 20 21 20 15 18 9 1 12"


def one_hundred_twelve(one: str, two: str):
    """
    Write a Python program to calculate the sum of two numbers given as strings. Return the result
    in the same string representation.
    """
    if not one.isdecimal() or not two.isdecimal():
        return False
    return str(int(one) + int(two))


print(one_hundred_twelve("234242342341", "2432342342"))
assert one_hundred_twelve("234242342341", "2432342342") == "236674684683"
assert one_hundred_twelve("", "2432342342") is False
assert one_hundred_twelve("1000", "0") == "1000"
assert one_hundred_twelve("1000", "10") == "1010"


def one_hundred_thirteen(string: str):
    """
    Write a Python program that returns a string sorted alphabetically by the first character of a
    given string of words.
    """
    return " ".join(sorted(string.split()))


print(one_hundred_thirteen("Calculate the sum of two said numbers given as strings."))
assert (
    one_hundred_thirteen("Red Green Black White Pink") == "Black Green Pink Red White"
)
assert (
    one_hundred_thirteen("Calculate the sum of two said numbers given as strings.")
    == "Calculate as given numbers of said strings. sum the two"
)
assert (
    one_hundred_thirteen("The quick brown fox jumps over the lazy dog.")
    == "The brown dog. fox jumps lazy over quick the"
)
