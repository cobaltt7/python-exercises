from typing import Any


def forty(data: list[str]):
    """Write a Python program to split a list based on the first character of a word."""
    output = {}
    for word in sorted(data):
        if word[0] not in output:
            output[word[0]] = []
        output[word[0]].append(word)
    return output


assert forty(
    [
        "be",
        "have",
        "do",
        "say",
        "get",
        "make",
        "go",
        "know",
        "take",
        "see",
        "come",
        "think",
        "look",
        "want",
        "give",
        "use",
        "find",
        "tell",
        "ask",
        "work",
        "seem",
        "feel",
        "leave",
        "call",
    ]
) == {
    "a": ["ask"],
    "b": ["be"],
    "c": ["call", "come"],
    "d": ["do"],
    "f": ["feel", "find"],
    "g": ["get", "give", "go"],
    "h": ["have"],
    "k": ["know"],
    "l": ["leave", "look"],
    "m": ["make"],
    "s": ["say", "see", "seem"],
    "t": ["take", "tell", "think"],
    "u": ["use"],
    "w": ["want", "work"],
}


def forty_one(count: int):
    """Write a Python program to create multiple lists."""
    return [[] for _ in range(count)]


print(forty_one(20))
assert forty_one(20) == [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]


def forty_two(one: list[Any], two: list[Any]):
    """Write a Python program to find missing and additional values in two lists."""
    return [
        [item for item in one if item not in two],
        [item for item in two if item not in one],
    ]


print(forty_two(["a", "b", "c", "d", "e", "f"], ["d", "e", "f", "g", "h"]))
assert forty_two(
    ["a", "b", "c", "d", "e", "f"],
    ["d", "e", "f", "g", "h"],
) == [["a", "b", "c"], ["g", "h"]]
assert forty_two(
    ["d", "e", "f", "g", "h"],
    ["a", "b", "c", "d", "e", "f"],
) == [["g", "h"], ["a", "b", "c"]]


def forty_three(data):
    """Write a Python program to split a list into different variables."""
    one, two, three = data

    print(one)
    print(two)
    print(three)


forty_three(
    [
        ("Black", "#000000", "rgb(0, 0, 0)"),
        ("Red", "#FF0000", "rgb(255, 0, 0)"),
        ("Yellow", "#FFFF00", "rgb(255, 255, 0)"),
    ]
)
