from typing import Any


def two_seven_one(data: list[Any]):
    """
    Write a Python program to check if there are duplicate values in a given flat list.
    """
    return len(set(data)) != len(data)


print(two_seven_one([1, 2, 3, 4, 5, 6, 7]))
assert two_seven_one([1, 2, 3, 4, 5, 6, 7]) is False
assert two_seven_one([1, 2, 3, 3, 4, 5, 5, 6, 7]) is True


def two_seven_two(step, end):
    """Generates a list of numbers in the arithmetic progression within a range."""
    return list(range(step, end + 1, step))


print(two_seven_two(1, 15))
assert two_seven_two(1, 15) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
assert two_seven_two(3, 37) == [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
assert two_seven_two(5, 25) == [5, 10, 15, 20, 25]


def two_seven_three(data: list[int]):
    """
    Write a Python program to find an element that divides a given list of integers
    with the same sum value.
    """
    for index, item in enumerate(data):
        if sum(data[:index]) == sum(data[index + 1 :]):
            return item
    return None


print(two_seven_three([0, 9, 2, 4, 5, 6]))
assert two_seven_three([0, 9, 2, 4, 5, 6]) == 4
assert two_seven_three([-4, 0, 6, 1, 0, 2]) == 1
assert two_seven_three([1, 2, 3, 4]) is None
assert two_seven_three([-4, 0, 5, 1, 0, 1]) == 1


def two_seven_four(data: list[str]):
    """
    Write a Python program to count the lowercase letters in a given list of words.
    """
    return len([letter for word in data for letter in word if letter.islower()])


print(two_seven_four(["Red", "Green", "Blue", "White"]))
assert two_seven_four(["Red", "Green", "Blue", "White"]) == 13
assert two_seven_four(["SQL", "C++", "C"]) == 0


def two_seven_five(data: list[float]):
    """
    Write a Python program to add all elements of a list of integers except the number
    at index. Return the updated string.
    """
    total = sum(data)
    return [total - number for number in data]


print(two_seven_five([0, 9, 2, 4, 5, 6]))
assert two_seven_five([0, 9, 2, 4, 5, 6]) == [26, 17, 24, 22, 21, 20]
assert two_seven_five([-4, 0, 6, 1, 0, 2]) == [9, 5, -1, 4, 5, 3]
assert two_seven_five([1, 2, 3]) == [5, 4, 3]
assert two_seven_five([-4, 0, 5, 1, 0, 1]) == [7, 3, -2, 2, 3, 2]


def two_seven_six(data: list[float]):
    """
    Write a Python program to find the largest odd number in a given list of integers.
    """
    return sorted((number for number in data if number % 2 == 1), reverse=True)[0]


print(two_seven_six([0, 9, 2, 4, 5, 6]))
assert two_seven_six([0, 9, 2, 4, 5, 6]) == 9
assert two_seven_six([-4, 0, 6, 1, 0, 2]) == 1
assert two_seven_six([1, 2, 3]) == 3
assert two_seven_six([-4, 0, 5, 1, 0, 1]) == 5


def two_seven_seven(data: list[float]):
    """
    Write a Python program to calculate the largest and smallest gap between sorted
    elements of a list of integers.
    """
    sorted_data = sorted(data)
    gaps = []
    for index, item in enumerate(sorted_data[:-1]):
        gaps.append(sorted_data[index + 1] - item)
    sorted_gaps = sorted(gaps)
    return (sorted_gaps[-1], sorted_gaps[0])


print(two_seven_seven([0, 9, 2, 4, 5, 6]))
assert two_seven_seven([0, 9, 2, 4, 5, 6]) == (3, 1)
assert two_seven_seven([23, -2, 45, 38, 12, 4, 6]) == (15, 2)
assert two_seven_seven([1, 2, 3]) == (1, 1)
assert two_seven_seven([-4, -3, 5, 20, 10, 1]) == (10, 1)


def two_seven_eight(data: list[int]):
    """
    Write a Python program to sum the missing numbers in a given list of integers.
    """
    return sum(range(data[0], data[-1] + 1)) - sum(data)


print(two_seven_eight([0, 3, 4, 7, 9]))
assert two_seven_eight([0, 3, 4, 7, 9]) == 22
assert two_seven_eight([44, 45, 48]) == 93
assert two_seven_eight([-7, -5, -4, 0]) == -12


def two_seven_nine(text: str, count: int):
    """
    Write a Python program to extract the first specified number of vowels from a given
    string. If the specified number is less than the number of vowels present in the
    string then display None.
    """
    vowels = [letter for letter in text if letter in "aeiouAEIOU"]
    if len(vowels) < count:
        return None
    return "".join(vowels[:count])


print(two_seven_nine("Python", 2))
assert two_seven_nine("Python", 2) is None
assert two_seven_nine("Python Exercises", 3) == "oEe"
assert two_seven_nine("AEIOU", 3) == "AEI"


def two_eight_zero(data: list[int]):
    """
    Write a Python program that takes a list of integers and finds all pairs of integers
    that differ by three. Return all pairs of integers in a list.
    """
    output = []
    for one in data:
        for two in data:
            if one + 3 == two:
                output.append([one, two])
    return output


print(two_eight_zero([0, -3, -5, -7, -8]))
assert two_eight_zero([0, 3, 4, 7, 9]) == [[0, 3], [4, 7]]
assert two_eight_zero([0, -3, -5, -7, -8]) == [[-3, 0], [-8, -5]]
assert two_eight_zero([1, 2, 3, 4, 5]) == [[1, 4], [2, 5]]
assert two_eight_zero([100, 102, 103, 114, 115]) == [[100, 103]]
