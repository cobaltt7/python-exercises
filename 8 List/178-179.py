from typing import Any


def one_seven_eight(data: list[Any], item: Any, interval: int):
    """
    Write a Python program to insert a specified element in a given list after every nth element.
    """
    start = data[:interval]
    if len(data) < interval:
        return start
    return start + [item] + one_seven_eight(data[interval:], item, interval)


print(one_seven_eight([1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0], 20, 4))
assert one_seven_eight(
    [1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0], 20, 4
) == [1, 3, 5, 7, 20, 9, 11, 0, 2, 20, 4, 6, 8, 10, 20, 8, 9, 0, 4, 20, 3, 0]
assert one_seven_eight(["s", "d", "f", "j", "s", "a", "j", "d", "f", "d"], "Z", 3) == [
    "s",
    "d",
    "f",
    "Z",
    "j",
    "s",
    "a",
    "Z",
    "j",
    "d",
    "f",
    "Z",
    "d",
]


def one_seven_nine(data: list[int]):
    """
    Write a Python program to create the largest possible number using the elements of a given list
    of positive integers.
    """
    numbers = sorted(
        (str(number) for number in data),
        key=lambda number: int(number) / (10 ** (len(number) - 1)),
        reverse=True,
    )
    return int("".join(numbers))


print(one_seven_nine([3, 40, 41, 43, 74, 9]))
assert one_seven_nine([3, 40, 41, 43, 74, 9]) == 9744341403
assert one_seven_nine([10, 40, 20, 30, 50, 60]) == 605040302010
assert one_seven_nine([910, 40, 120, 30, 504, 60]) == 910605044030120
assert one_seven_nine([8, 4, 2, 9, 5, 6, 1, 0]) == 98654210
