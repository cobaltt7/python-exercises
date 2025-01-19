from math import floor


def fortyTwo(data):
    """
    Write a Python program to find the set of distinct characters in a given string, ignoring case.
    """
    return sorted(set(data.lower()))


def fortyThree(data):
    """Write a Python program to find all words in a given string with n consonants."""

    def predicate(word):
        filtered = filter(lambda char: char not in "aeiou", word)
        return len(list(filtered)) == data

    STRING = "this is our time"
    return list(filter(predicate, STRING.split()))


def fortyFour(data):
    """
    Write a Python program to find which characters of a hexadecimal number correspond to prime
    numbers.
    """

    def isPrime(number):
        if number < 2:
            return False
        for i in range(2, floor(number / 2) + 1):
            if number % i == 0:
                return False
        return True

    return list(map(lambda digit: isPrime(int(digit, 16)), data))


assert fortyTwo("HELLO") == ["e", "h", "l", "o"]
assert fortyTwo("HelLo") == ["e", "h", "l", "o"]
assert fortyTwo("Ignoring case") == [" ", "a", "c", "e", "g", "i", "n", "o", "r", "s"]

assert fortyThree(3) == ["this"]
assert fortyThree(2) == ["time"]
assert fortyThree(1) == ["is", "our"]

assert fortyFour("123ABCD") == [False, True, True, False, True, False, True]
assert fortyFour("123456") == [False, True, True, False, True, False]
assert fortyFour("FACE") == [False, False, False, False]
