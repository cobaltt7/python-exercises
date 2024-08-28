def one(numbers):
    """Write a Python program to calculate the sum of a list of numbers."""
    if not len(numbers):
        return 0
    return numbers[0] + one(numbers[1:])


print(one([29, 40, 37, 35, 37, 29]))
assert one([29, 40, 37, 35, 37, 29]) == 207


def two(number, base):
    """Write a Python program to convert an integer to a string in any base."""
    characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"
    if number < base:
        return characters[number]
    else:
        return two(number // base, base) + characters[number % base]


print(two(2835, 16))
assert two(2835, 16) == "B13"
