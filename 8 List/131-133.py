from typing import Any


def one_three_one(data: list[Any]):
    """
    Write a Python program to count the frequency of consecutive duplicate elements in a given list
    of numbers.
    """
    if not data:
        return ([], [])
    items = [data[0]]
    counts = [0]
    for item in data:
        if item == items[-1]:
            counts[-1] += 1
        else:
            items.append(item)
            counts.append(1)
    return (items, counts)


print(one_three_one([1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]))
assert one_three_one([1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]) == ([1, 2, 4, 5], [1, 3, 3, 4])


def one_three_two(data: list[float]):
    """
    Write a Python program to find all index positions of the maximum and minimum values in a given
    list of numbers.
    """
    numbers = sorted(data)
    min_number = numbers[0]
    max_number = numbers[-1]

    min_indicies = []
    max_indicies = []
    for index, number in enumerate(data):
        if number == min_number:
            min_indicies.append(index)
        if number == max_number:
            max_indicies.append(index)

    return (max_indicies, min_indicies)


print(one_three_two([12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]))
assert one_three_two([12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]) == (
    [7],
    [3, 11],
)
