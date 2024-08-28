from typing import Any


def eight_two(data: list[Any], length: int):
    """
    Write a Python program to generate the combinations of n distinct objects taken from the
    elements of a given list.
    """
    if length == 0:
        return []
    if length == 1:
        return data

    output = []
    for index, item in enumerate(data):
        for other in eight_two(data[index + 1 :], length - 1):
            others = [other] if length == 2 else other
            output.append((item, *others))
    return output


print(eight_two([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
assert eight_two([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == [
    (1, 2, 3),
    (1, 2, 4),
    (1, 2, 5),
    (1, 2, 6),
    (1, 2, 7),
    (1, 2, 8),
    (1, 2, 9),
    (1, 3, 4),
    (1, 3, 5),
    (1, 3, 6),
    (1, 3, 7),
    (1, 3, 8),
    (1, 3, 9),
    (1, 4, 5),
    (1, 4, 6),
    (1, 4, 7),
    (1, 4, 8),
    (1, 4, 9),
    (1, 5, 6),
    (1, 5, 7),
    (1, 5, 8),
    (1, 5, 9),
    (1, 6, 7),
    (1, 6, 8),
    (1, 6, 9),
    (1, 7, 8),
    (1, 7, 9),
    (1, 8, 9),
    (2, 3, 4),
    (2, 3, 5),
    (2, 3, 6),
    (2, 3, 7),
    (2, 3, 8),
    (2, 3, 9),
    (2, 4, 5),
    (2, 4, 6),
    (2, 4, 7),
    (2, 4, 8),
    (2, 4, 9),
    (2, 5, 6),
    (2, 5, 7),
    (2, 5, 8),
    (2, 5, 9),
    (2, 6, 7),
    (2, 6, 8),
    (2, 6, 9),
    (2, 7, 8),
    (2, 7, 9),
    (2, 8, 9),
    (3, 4, 5),
    (3, 4, 6),
    (3, 4, 7),
    (3, 4, 8),
    (3, 4, 9),
    (3, 5, 6),
    (3, 5, 7),
    (3, 5, 8),
    (3, 5, 9),
    (3, 6, 7),
    (3, 6, 8),
    (3, 6, 9),
    (3, 7, 8),
    (3, 7, 9),
    (3, 8, 9),
    (4, 5, 6),
    (4, 5, 7),
    (4, 5, 8),
    (4, 5, 9),
    (4, 6, 7),
    (4, 6, 8),
    (4, 6, 9),
    (4, 7, 8),
    (4, 7, 9),
    (4, 8, 9),
    (5, 6, 7),
    (5, 6, 8),
    (5, 6, 9),
    (5, 7, 8),
    (5, 7, 9),
    (5, 8, 9),
    (6, 7, 8),
    (6, 7, 9),
    (6, 8, 9),
    (7, 8, 9),
]
assert eight_two([1, 2, 3, 4, 5, 6, 7, 8, 9], 2) == [
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (1, 6),
    (1, 7),
    (1, 8),
    (1, 9),
    (2, 3),
    (2, 4),
    (2, 5),
    (2, 6),
    (2, 7),
    (2, 8),
    (2, 9),
    (3, 4),
    (3, 5),
    (3, 6),
    (3, 7),
    (3, 8),
    (3, 9),
    (4, 5),
    (4, 6),
    (4, 7),
    (4, 8),
    (4, 9),
    (5, 6),
    (5, 7),
    (5, 8),
    (5, 9),
    (6, 7),
    (6, 8),
    (6, 9),
    (7, 8),
    (7, 9),
    (8, 9),
]


def eight_three(data: list[float]):
    """
    Write a Python program to round every number in a given list of numbers and print the total sum
    multiplied by the length of the list.
    """
    return sum(round(number) for number in data) * len(data)


print(eight_three([22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]))
assert eight_three([22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]) == 243


def eight_four(data: list[float]):
    """
    Write a Python program to extract a given number of randomly selected elements from a given
    list.
    """
    numbers = [round(number) for number in data]
    return [
        min(numbers),
        max(numbers),
        " ".join(str(number * 5) for number in sorted(numbers)),
    ]


print(eight_four([22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]))
assert (eight_four([22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5])) == [
    4,
    22,
    "20 25 45 55 60 70 80 90 110",
]
