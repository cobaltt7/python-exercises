from math import floor


def seventyFour(data):
    """
    Write a Python program to find a string consisting of space-separated characters with given
    counts.
    """
    letters = enumerate(data.keys())
    counts = list(data.values())
    return " ".join(map(lambda entry: " ".join([entry[1]] * counts[entry[0]]), letters))


print(seventyFour({"f": 1, "o": 2}))
assert seventyFour({"f": 1, "o": 2}) == "f o o"
assert seventyFour({"a": 1, "b": 1, "c": 1}) == "a b c"


def seventyFive(data):
    """
    Write a Python program to reorder numbers from a given array in increasing/decreasing order
    based on whether the first plus last element is odd/even.
    """
    return sorted(data, reverse=not (data[0] + data[-1]) % 2)


print(seventyFive([3, 7, 4]))
assert seventyFive([3, 7, 4]) == [3, 4, 7]
assert seventyFive([2, 7, 4]) == [7, 4, 2]
assert seventyFive([1, 5, 6, 7, 4, 2, 8]) == [1, 2, 4, 5, 6, 7, 8]
assert seventyFive([1, 5, 6, 7, 4, 2, 9]) == [9, 7, 6, 5, 4, 2, 1]


def seventySix(data):
    """
    Write a Python program to find the index of the largest prime in the list and the sum of its
    digits.
    """

    def isPrime(number):
        if number < 2:
            return False
        for i in range(2, floor(number / 2) + 1):
            if number % i == 0:
                return False
        return True

    primes = filter(lambda entry: isPrime(entry[1]), enumerate(data))
    largest = sorted(primes, reverse=True, key=lambda entry: entry[1])[0]
    return [largest[0], sum(map(int, str(largest[1])))]


print(seventySix([23, 17, 201, 14, 10473, 43225, 421, 423, 11, 10, 2022, 342157]))
assert seventySix([3, 7, 4]) == [1, 7]
assert seventySix([3, 11, 7, 17, 19, 4]) == [4, 10]
assert seventySix([23, 17, 201, 14, 10473, 43225, 421, 423, 11, 10, 2022, 342157]) == [
    6,
    7,
]
