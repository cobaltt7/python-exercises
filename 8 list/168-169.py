from typing import Any


def one_six_eight(data: list[str | list[str | float]]):
    """
    Write a Python program to display vertically each element of a given list, list of lists.
    """
    lists = data if isinstance(data[0], list) else [data]
    print(lists)
    return "\n".join(
        " ".join(str(sublist[index]) for sublist in lists)
        for index in range(len(lists[0]))
    )


print(one_six_eight(["a", "b", "c", "d", "e", "f"]))
assert one_six_eight(["a", "b", "c", "d", "e", "f"]) == """a
b
c
d
e
f"""
assert one_six_eight([[1, 2, 5], [4, 5, 8], [7, 3, 6]]) == """1 4 7
2 5 3
5 8 6"""
assert (
    one_six_eight([["a", "b", "c", "d"], ["e", "f", "g", "h"], ["j", "k", "l", "m"]])
    == """a e j
b f k
c g l
d h m"""
)


def one_six_nine(data: list[Any]):
    """
    Write a Python program to convert a given list of strings and characters to a single list of
    characters.
    """
    return [element for sublist in data for element in sublist]


print(one_six_nine(["red", "white", "a", "b", "black", "f"]))
assert one_six_nine(["red", "white", "a", "b", "black", "f"]) == [
    "r",
    "e",
    "d",
    "w",
    "h",
    "i",
    "t",
    "e",
    "a",
    "b",
    "b",
    "l",
    "a",
    "c",
    "k",
    "f",
]
