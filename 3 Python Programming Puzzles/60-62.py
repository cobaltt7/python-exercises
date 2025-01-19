from math import floor


def sixty(data):
    """
    Write a Python program to find a list of all numbers that are adjacent to a prime number in the
    list, sorted without duplicates.
    """

    def isPrime(number):
        if number < 2:
            return False
        for i in range(2, floor(number / 2) + 1):
            if number % i == 0:
                return False
        return True

    output = [
        entry[1]
        for entry in enumerate(data)
        if (entry[0] > 0 and isPrime(data[entry[0] - 1]))
        or (entry[0] + 1 != len(data) and isPrime(data[entry[0] + 1]))
    ]
    return sorted(set(output))


print(sixty([1, 2, 3, 5, 1, 16, 7, 11, 4]))
assert sixty([2, 17, 16, 0, 6, 4, 5]) == [2, 4, 16, 17]
assert sixty([1, 2, 19, 16, 6, 4, 10]) == [1, 2, 16, 19]
assert sixty([1, 2, 3, 5, 1, 16, 7, 11, 4]) == [1, 2, 3, 4, 5, 7, 11, 16]


def sixtyOne(data):
    """
    Write a Python program to find the number which when appended to the list makes the total 0.
    """
    summed = sum(data)
    return 0 - summed


print(sixtyOne([1, 2, 3, 4, 5]))
assert sixtyOne([1, 2, 3, 4, 5]) == -15
assert sixtyOne([-1, -2, -3, -4, 5]) == 5
assert sixtyOne([10, 42, 17, 9, 1315182, 184, 102, 29, 15, 39, 755]) == -1316384


def sixtyTwo(data):
    """
    Write a Python program to find the dictionary key whose case is different from all other keys.
    """
    keys = sorted(data.keys())
    return keys[-1 if keys[1].isupper() else 0]


print(sixtyTwo({"red": "", "GREEN": "", "blue": "orange"}))
assert sixtyTwo({"red": "", "GREEN": "", "blue": "orange"}) == "GREEN"
assert sixtyTwo({"RED": "", "GREEN": "", "orange": "#125GD"}) == "orange"
