from math import floor


def sixtyThree(data):
    """
    Write a Python program to find the sum of the even elements that are at odd indices in a given
    list.
    """
    return sum(
        [entry[1] for entry in enumerate(data) if entry[0] % 2 and not entry[1] % 2]
    )


print(sixtyThree([1, 2, 8, 3, 9, 4]))
assert sixtyThree([1, 2, 3, 4, 5, 6, 7]) == 12
assert sixtyThree([1, 2, 8, 3, 9, 4]) == 6


def sixtyFour(data):
    """
    Write a Python program to find the string consisting of all the words whose lengths are prime
    numbers.
    """

    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, floor(number / 2) + 1):
            if number % i == 0:
                return False
        return True

    return " ".join(filter(lambda word: is_prime(len(word)), data.split()))


print(sixtyFour("The quick brown fox jumps over the lazy dog."))
assert (
    sixtyFour("The quick brown fox jumps over the lazy dog.")
    == "The quick brown fox jumps the"
)
assert (
    sixtyFour("Foreign Flights Won't Resume On Dec 15, Decision Later.")
    == "Foreign Flights Won't On Dec 15,"
)


def sixtyFive(n, shift):
    """
    Write a Python program to shift the decimal digits n places to the left, wrapping the extra
    digits around. If the shift > the number of digits in n, reverse the string.
    """
    string = str(n)
    if shift > len(string):
        return int("".join(reversed(string)))
    left = string[shift:]
    right = string[:shift]
    return int(left + right)


print(sixtyFive(12345, 6))
assert sixtyFive(12345, 1) == 23451
assert sixtyFive(12345, 2) == 34512
assert sixtyFive(12345, 3) == 45123
assert sixtyFive(12345, 5) == 12345
assert sixtyFive(12345, 6) == 54321
