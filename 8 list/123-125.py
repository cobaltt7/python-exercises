def one_two_three(data: list[str]):
    """Write a Python program to reverse strings in a given list of string values."""
    return [item[::-1] for item in data]


print(one_two_three(["Red", "Green", "Blue", "White", "Black"]))
assert one_two_three(["Red", "Green", "Blue", "White", "Black"]) == [
    "deR",
    "neerG",
    "eulB",
    "etihW",
    "kcalB",
]


def one_two_four(data: list[tuple[float, float]]):
    """
    Write a Python program to find the maximum and minimum product from the pairs of tuple within a
    given list.
    """
    numbers = sorted(entry[0] * entry[1] for entry in data)
    return (numbers[-1], numbers[0])


print(one_two_four([(2, 7), (2, 6), (1, 8), (4, 9)]))
assert one_two_four([(2, 7), (2, 6), (1, 8), (4, 9)]) == (36, 8)


def one_two_five(data: list[float]):
    """Write a Python program to calculate the product of the unique numbers of a given list."""
    output = 1
    for number in set(data):
        output *= number
    return output


print(one_two_five([10, 20, 30, 40, 20, 50, 60, 40]))
assert one_two_five([10, 20, 30, 40, 20, 50, 60, 40]) == 720000000
