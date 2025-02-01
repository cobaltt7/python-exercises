from typing import Any


def nine_two(one: list[list[Any]], two: list[list[Any]]):
    """Write a Python program to check if a nested list is a subset of another nested list."""
    return all(sublist in one for sublist in two)


print(nine_two([[1, 3], [5, 7], [9, 11], [13, 15, 17]], [[1, 3], [13, 15, 17]]))
assert nine_two([[1, 3], [5, 7], [9, 11], [13, 15, 17]], [[1, 3], [13, 15, 17]]) is True
assert nine_two([[[1, 2], [2, 3]], [[3, 4], [5, 6]]], [[[3, 4], [5, 6]]]) is True
assert nine_two([[[1, 2], [2, 3]], [[3, 4], [5, 7]]], [[[3, 4], [5, 6]]]) is False
assert (
    nine_two([[1, 3], [5, 7], [9, 11], [13, 15, 17]], [[1, 2], [13, 15, 16]]) is False
)


def nine_three(lists: list[list[Any]], element: Any):
    """Write a Python program to count the number of sublists contain a particular element."""
    return sum(int(element in sublist) for sublist in lists)


print(nine_three([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 1))
assert nine_three([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 1) == 3
assert nine_three([[1, 3], [5, 7], [1, 11], [1, 15, 1, 7]], 1) == 3
assert nine_three([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 7) == 2
assert nine_three([["A", "B"], ["A", "C"], ["A", "D", "E"], ["B", "C", "D"]], "A") == 3
assert nine_three([["A", "B"], ["A", "C"], ["A", "D", "E"], ["B", "C", "D"]], "E") == 1


def nine_four(data: list[list[Any]]):
    """Write a Python program to count number of unique sublists within a given list."""
    output = {}
    for sublist in data:
        hashable = tuple(sublist)
        if hashable not in output:
            output[hashable] = 0
        output[hashable] += 1
    return output


print(nine_four([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]))
assert nine_four([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]) == {
    (1, 3): 2,
    (5, 7): 2,
    (13, 15, 17): 1,
    (9, 11): 1,
}
assert nine_four([["green", "orange"], ["black"], ["green", "orange"], ["white"]]) == {
    ("green", "orange"): 2,
    ("black",): 1,
    ("white",): 1,
}
