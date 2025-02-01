from typing import Any, List


def one_nine_nine(data: List[str]):
    """
    Write a Python program to convert a Unicode list to a list of strings.
    """
    return data  # Strings are Unicode strings by default in Python 3


print(one_nine_nine(["S001", "S002", "S003", "S004"]))
assert one_nine_nine(["S001", "S002", "S003", "S004"]) == [
    "S001",
    "S002",
    "S003",
    "S004",
]


def two_zero_zero(data: List[Any]):
    """Write a Python program to pair consecutive elements of a given list."""
    length = len(data)
    return [
        [item, data[index + 1]] for index, item in enumerate(data) if index < length - 1
    ]


print(two_zero_zero([1, 2, 3, 4, 5, 6]))
assert two_zero_zero([1, 2, 3, 4, 5, 6]) == [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
assert two_zero_zero([1, 2, 3, 4, 5]) == [[1, 2], [2, 3], [3, 4], [4, 5]]


def two_zero_one(string: str, search: List[str]):
    """
    Write a Python program to check if a given string contains an element that is present in a list.
    """
    return any(item in string for item in search)


print(
    two_zero_one(
        "https://www.w3resource.com/python-exercises/list/", [".com", ".edu", ".tv"]
    )
)
assert two_zero_one(
    "https://www.w3resource.com/python-exercises/list/", [".com", ".edu", ".tv"]
)
assert not two_zero_one("https://www.w3resource.net", [".com", ".edu", ".tv"])


def two_zero_two(data: List[Any]):
    """Write a Python program to find the indexes of all None items in a given list."""
    return [index for index, item in enumerate(data) if item is None]


print(two_zero_two([1, None, 5, 4, None, 0, None, None]))
assert two_zero_two([1, None, 5, 4, None, 0, None, None]) == [1, 4, 6, 7]


def two_zero_three(data: List[str]):
    """Write a Python program to join adjacent members of a given list."""
    return [data[index - 1] + item for index, item in enumerate(data) if index % 2 == 1]


print(two_zero_three(["1", "2", "3", "4", "5", "6", "7", "8"]))
assert two_zero_three(["1", "2", "3", "4", "5", "6", "7", "8"]) == [
    "12",
    "34",
    "56",
    "78",
]
assert two_zero_three(["1", "2", "3"]) == ["12"]


def two_zero_four(data: List[str | float]):
    """
    Write a Python program to check if the first digit or character of each element in a list is the
    same.
    """
    if not data:
        return True
    character = str(data[0])[0]
    return all(str(item)[0] == character for item in data[1:])


print(two_zero_four([1234, 122, 1984, 19372, 100]))
assert two_zero_four([1234, 122, 1984, 19372, 100])
assert not two_zero_four([1234, 922, 1984, 19372, 100])
assert two_zero_four(["aabc", "abc", "ab", "a"])
assert not two_zero_four(["aabc", "abc", "ab", "ha"])


def two_zero_five(data: List[float], threshold: float):
    """
    Write a Python program to find the indices of elements in a given list that are greater than a
    specified value.
    """
    return [index for index, item in enumerate(data) if item > threshold]


print(two_zero_five([1234, 1522, 1984, 19372, 1000, 2342, 7626], 3000))
assert two_zero_five([1234, 1522, 1984, 19372, 1000, 2342, 7626], 3000) == [3, 6]
assert two_zero_five([1234, 1522, 1984, 19372, 1000, 2342, 7626], 20000) == []


def two_zero_six(data: List[str]):
    """Write a Python program to remove additional spaces from a given list."""
    return [item.strip() for item in data]


print(two_zero_six(["abc ", " ", " ", "sdfds ", " ", " ", "sdfds ", "huy"]))
assert two_zero_six(["abc ", " ", " ", "sdfds ", " ", " ", "sdfds ", "huy"]) == [
    "abc",
    "",
    "",
    "sdfds",
    "",
    "",
    "sdfds",
    "huy",
]


def two_zero_seven(one: List[tuple[Any, Any]], two: List[tuple[Any, Any]]):
    """Write a Python program to find the common tuples between two given lists."""
    return set(item for item in one if item in two)


print(
    two_zero_seven(
        [("red", "green"), ("black", "white"), ("orange", "pink")],
        [("red", "green"), ("orange", "pink")],
    )
)
assert two_zero_seven(
    [("red", "green"), ("black", "white"), ("orange", "pink")],
    [("red", "green"), ("orange", "pink")],
) == {("orange", "pink"), ("red", "green")}
assert two_zero_seven(
    [("red", "green"), ("orange", "pink")],
    [("red", "green"), ("black", "white"), ("orange", "pink")],
) == {("orange", "pink"), ("red", "green")}


def two_zero_eight(data: List[float]):
    """
    Sum a list of numbers. Write a Python program to sum the first number with the second and divide
    it by 2, then sum the second with the third and divide by 2, and so on.
    """
    max_index = len(data) - 1
    return [
        (item + data[index + 1]) / 2
        for index, item in enumerate(data)
        if index < max_index
    ]


print(two_zero_eight([1, 2, 3, 4, 5, 6, 7]))
assert two_zero_eight([1, 2, 3, 4, 5, 6, 7]) == [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
assert two_zero_eight([0, 1, -3, 3, 7, -5, 6, 7, 11]) == [
    0.5,
    -1.0,
    0.0,
    5.0,
    1.0,
    0.5,
    6.5,
    9.0,
]
