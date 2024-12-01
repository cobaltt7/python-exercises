from typing import Any


def one_eight_three(data: list[list[Any]]):
    """Write a Python program to get the unique values in a given list of lists."""
    return set(item for sublist in data for item in sublist)


print(
    one_eight_three(
        [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
    )
)
assert one_eight_three(
    [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
) == {0, 1, 2, 3, 4, 5, 7}

assert one_eight_three(
    [
        ["h", "g", "l", "k"],
        ["a", "b", "d", "e", "c"],
        ["j", "i", "y"],
        ["n", "b", "v", "c"],
        ["x", "z"],
    ]
) == {"e", "d", "c", "b", "x", "k", "n", "h", "g", "j", "i", "a", "l", "y", "v", "z"}


def one_eight_four(data: list[str]):
    """
    Write a Python program to form Bigrams of words in a given list of strings.


    From Wikipedia:

    A bigram or digram is a sequence of two adjacent elements from a string of tokens, which are
    typically letters, syllables, or words. A bigram is an n-gram for n=2. The frequency
    distribution of every bigram in a string is commonly used for simple statistical analysis of
    text in many applications, including in computational linguistics, cryptography, speech
    recognition, and so on.
    """
    output = []
    for string in data:
        words = string.split()
        for index, word in enumerate(words[:-1]):
            output.append((word, words[index + 1]))
    return output


print(
    one_eight_four(
        ["Sum all the items in a list", "Find the second smallest number in a list"]
    )
)
assert one_eight_four(
    ["Sum all the items in a list", "Find the second smallest number in a list"]
) == [
    ("Sum", "all"),
    ("all", "the"),
    ("the", "items"),
    ("items", "in"),
    ("in", "a"),
    ("a", "list"),
    ("Find", "the"),
    ("the", "second"),
    ("second", "smallest"),
    ("smallest", "number"),
    ("number", "in"),
    ("in", "a"),
    ("a", "list"),
]


def one_eight_five(data: int):
    """Write a Python program to convert a given decimal number to binary list."""
    return [int(digit) for digit in bin(data)[2:]]


print(one_eight_five(8))
assert one_eight_five(8) == [1, 0, 0, 0]
assert one_eight_five(45) == [1, 0, 1, 1, 0, 1]
assert one_eight_five(100) == [1, 1, 0, 0, 1, 0, 0]
