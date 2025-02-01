from typing import Any


def eight(data: list[Any]):
    """Write a Python program to check if a list is empty or not."""
    return not data


print(eight([]))
assert eight(["abc", "xyz", "aba", "1221"]) is False
assert eight([]) is True


def nine(data: list[Any]):
    """Write a Python program to clone or copy a list."""
    return list(data)


original = [0, 1, 2, 3, 4]
copy = nine(original)
print(copy)
assert copy == original
copy[0] = 1
print(copy, original)
assert copy[0] == 1
assert original[0] == 0


def ten(data: str, n: int):
    """
    Write a Python program to find the list of words that are longer than n from a given list of
    words.
    """
    return [word for word in data.split() if len(word) > n]


print(ten("The quick brown fox jumps over the lazy dog", 3))
assert ten("The quick brown fox jumps over the lazy dog", 3) == [
    "quick",
    "brown",
    "jumps",
    "over",
    "lazy",
]
