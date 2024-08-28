from typing import Any


def one_six_one(data: list[int], remove_one=True):
    """
    Write a Python program to check if a given list increases strictly. Moreover, if removing only
    one element from the list results in a strictly increasing list, we still consider the list
    true.
    """
    if not data:
        return True

    index = data[0]
    has_removed = not remove_one
    for item in data[1:]:
        if item == index + 1:
            index = item
        else:
            if has_removed:
                return one_six_one(data[1:], False) if remove_one else False
            has_removed = True
    return True


print(one_six_one([1, 2, 3, 0, 4, 5, 6]))
assert one_six_one([]) is True
assert one_six_one([1]) is True
assert one_six_one([1, 2]) is True
assert one_six_one([1, 2, 3]) is True
assert one_six_one([3, 1, 2]) is True
assert one_six_one([1, 2, 3, 0, 4, 5, 6]) is True
assert one_six_one([1, 2, 3, 0]) is True
assert one_six_one([1, 2, 0, 3]) is True
assert one_six_one([10, 1, 2, 3, 4, 5]) is True
assert one_six_one([1, 2, 10, 3, 4]) is True
assert one_six_one([1, 2, 3, 12, 4, 5]) is True
assert one_six_one([3, 2, 1]) is False
assert one_six_one([1, 2, 0, -1]) is False
assert one_six_one([5, 6, 1, 2]) is False
assert one_six_one([1, 2, 3, 0, -1]) is False
assert one_six_one([10, 11, 12, 2, 3, 4, 5]) is False


def one_six_two(data: list[Any], search: Any):
    """Write a Python program to find the last occurrence of a specified item in a given list."""
    return len(data) - data[::-1].index(search) - 1


print(
    one_six_two(
        [
            "s",
            "d",
            "f",
            "s",
            "d",
            "f",
            "s",
            "f",
            "k",
            "o",
            "p",
            "i",
            "w",
            "e",
            "k",
            "c",
        ],
        "f",
    )
)
assert (
    one_six_two(
        [
            "s",
            "d",
            "f",
            "s",
            "d",
            "f",
            "s",
            "f",
            "k",
            "o",
            "p",
            "i",
            "w",
            "e",
            "k",
            "c",
        ],
        "f",
    )
    == 7
)
assert (
    one_six_two(
        [
            "s",
            "d",
            "f",
            "s",
            "d",
            "f",
            "s",
            "f",
            "k",
            "o",
            "p",
            "i",
            "w",
            "e",
            "k",
            "c",
        ],
        "c",
    )
    == 15
)
assert (
    one_six_two(
        [
            "s",
            "d",
            "f",
            "s",
            "d",
            "f",
            "s",
            "f",
            "k",
            "o",
            "p",
            "i",
            "w",
            "e",
            "k",
            "c",
        ],
        "k",
    )
    == 14
)
assert (
    one_six_two(
        [
            "s",
            "d",
            "f",
            "s",
            "d",
            "f",
            "s",
            "f",
            "k",
            "o",
            "p",
            "i",
            "w",
            "e",
            "k",
            "c",
        ],
        "w",
    )
    == 12
)
