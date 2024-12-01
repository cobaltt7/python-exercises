from typing import Any, List


def one_eight_nine(data: List[Any]):
    """
    Write a Python program to shift last element to first position and first element to last
    position in a given list.
    """
    return data[-1:] + data[1:-1] + data[:1]


print(one_eight_nine([1, 2, 3, 4, 5, 6, 7]))
assert one_eight_nine([1, 2, 3, 4, 5, 6, 7]) == [7, 2, 3, 4, 5, 6, 1]
assert one_eight_nine(["s", "d", "f", "d", "s", "s", "d", "f"]) == [
    "f",
    "d",
    "f",
    "d",
    "s",
    "s",
    "d",
    "s",
]


def one_nine_zero(one: List[float], two: List[float], count: int):
    """
    Write a Python program to find the specified number of largest products from two given lists,
    multiplying an element from each list.
    """
    output = []
    for item_one in one:
        for item_two in two:
            output.append(item_one * item_two)
    return sorted(output, reverse=True)[:count]


print(one_nine_zero([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 3))
assert one_nine_zero([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 3) == [60, 54, 50]
assert one_nine_zero([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 4) == [60, 54, 50, 48]


def one_nine_one(one: List[float], two: List[float], three: List[float]):
    """Write a Python program to find the maximum and minimum values of the three given lists."""
    numbers = one + two + three
    return (max(numbers), min(numbers))


print(one_nine_one([2, 3, 5, 8, 7, 2, 3], [4, 3, 9, 0, 4, 3, 9], [2, 1, 5, 6, 5, 5, 4]))
assert one_nine_one(
    [2, 3, 5, 8, 7, 2, 3], [4, 3, 9, 0, 4, 3, 9], [2, 1, 5, 6, 5, 5, 4]
) == (9, 0)


def one_nine_two(data: List[tuple[Any, ...]]):
    """Write a Python program to remove all strings from a given list of tuples."""
    return [
        tuple(item for item in tuple_item if not isinstance(item, str))
        for tuple_item in data
    ]


print(
    one_nine_two(
        [
            (100, "Math"),
            (80, "Math"),
            (90, "Math"),
            (88, "Science", 89),
            (90, "Science", 92),
        ]
    )
)
assert one_nine_two(
    [
        (100, "Math"),
        (80, "Math"),
        (90, "Math"),
        (88, "Science", 89),
        (90, "Science", 92),
    ]
) == [(100,), (80,), (90,), (88, 89), (90, 92)]


def one_nine_three(data: List[List[Any]]):
    """Write a Python program to find the dimension of a given matrix."""
    return (len(data), len(data[0]))


print(one_nine_three([[1, 2], [2, 4]]))
assert one_nine_three([[1, 2], [2, 4]]) == (2, 2)
assert one_nine_three([[0, 1, 2], [2, 4, 5]]) == (2, 3)
assert one_nine_three([[0, 1, 2], [2, 4, 5], [2, 3, 4]]) == (3, 3)


def one_nine_four(lists: List[List[float]]):
    """
    Write a Python program to sum two or more lists. The lengths of the lists may be different.
    """
    return [
        sum(sublist[index] if len(sublist) > index else 0 for sublist in lists)
        for index in range(max(len(numbers) for numbers in lists))
    ]


print(one_nine_four([[1, 2, 4], [2, 4, 4], [1, 2]]))
assert one_nine_four([[1, 2, 4], [2, 4, 4], [1, 2]]) == [4, 8, 8]
assert one_nine_four([[1], [2, 4, 4], [1, 2], [4]]) == [8, 6, 4]


def one_nine_five(data: List[Any]):
    """
    Write a Python program to traverse a given list in reverse order, and print the elements with
    the original index.
    """
    length = len(data) - 1
    return [(length - index, item) for index, item in enumerate(data[::-1])]


print(one_nine_five(["red", "green", "white", "black"]))
assert one_nine_five(["red", "green", "white", "black"]) == [
    (3, "black"),
    (2, "white"),
    (1, "green"),
    (0, "red"),
]


def one_nine_six(data: List[Any], search: Any):
    """Write a Python program to move a specified element in a given list."""
    return [item for item in data if item != search] + [search]


print(one_nine_six(["red", "green", "white", "black", "orange"], "white"))
assert one_nine_six(["red", "green", "white", "black", "orange"], "white") == [
    "red",
    "green",
    "black",
    "orange",
    "white",
]
assert one_nine_six(["red", "green", "white", "black", "orange"], "red") == [
    "green",
    "white",
    "black",
    "orange",
    "red",
]
assert one_nine_six(["red", "green", "white", "black", "orange"], "black") == [
    "red",
    "green",
    "white",
    "orange",
    "black",
]


def one_nine_seven(lists: List[List[float]]):
    """
    Write a Python program to compute the average of the n-th element in a given list of lists with
    different lengths.
    """
    return [
        sum(numbers) / len(numbers)
        for numbers in [
            [sublist[index] for sublist in lists if len(sublist) > index]
            for index in range(max(len(numbers) for numbers in lists))
        ]
    ]


print(
    one_nine_seven(
        [[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
    )
)
assert one_nine_seven(
    [[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
) == [4.8, 5.8, 6.8, 8.0, 11.0]


def one_nine_eight(one: List[Any], two: List[Any]):
    """
    Write a Python program to compare two given lists and find the indices of the values present in
    both lists.
    """
    return [index for index, item in enumerate(one) if item in two]


print(one_nine_eight([1, 2, 3, 4, 5, 6], [7, 8, 5, 2, 10, 12]))
assert one_nine_eight([1, 2, 3, 4, 5, 6], [7, 8, 5, 2, 10, 12]) == [1, 4]
assert one_nine_eight([1, 2, 3, 4, 5, 6], [7, 8, 5, 7, 10, 12]) == [4]
assert not one_nine_eight([1, 2, 3, 4, 15, 6], [7, 8, 5, 7, 10, 12])
