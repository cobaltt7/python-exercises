from typing import Any, Hashable


def one_six(obj: Any):
    """Write a Python program to get a dictionary from an object's fields."""
    return obj.__dict__


class dictObj(object):
    def __init__(self):
        self.x = "red"
        self.y = "Yellow"
        self.z = "Green"


print(one_six(dictObj()))
assert one_six(dictObj()) == {"x": "red", "y": "Yellow", "z": "Green"}


def one_seven(data: dict):
    """Write a Python program to remove duplicates from the dictionary."""
    output: dict = {}
    for key in data:
        if data[key] not in output.values():
            output[key] = data[key]
    return output


print(
    one_seven({
        "id1": {
            "name": ["Sara"],
            "class": ["V"],
            "subject_integration": ["english", "math", "science"],
        },
        "id2": {
            "name": ["David"],
            "class": ["V"],
            "subject_integration": ["english", "math", "science"],
        },
        "id3": {
            "name": ["Sara"],
            "class": ["V"],
            "subject_integration": ["english", "math", "science"],
        },
        "id4": {
            "name": ["Surya"],
            "class": ["V"],
            "subject_integration": ["english", "math", "science"],
        },
    })
)
assert one_seven({
    "id1": {
        "name": ["Sara"],
        "class": ["V"],
        "subject_integration": ["english", "math", "science"],
    },
    "id2": {
        "name": ["David"],
        "class": ["V"],
        "subject_integration": ["english", "math", "science"],
    },
    "id3": {
        "name": ["Sara"],
        "class": ["V"],
        "subject_integration": ["english", "math", "science"],
    },
    "id4": {
        "name": ["Surya"],
        "class": ["V"],
        "subject_integration": ["english", "math", "science"],
    },
}) == {
    "id2": {
        "subject_integration": ["english", "math", "science"],
        "class": ["V"],
        "name": ["David"],
    },
    "id4": {
        "subject_integration": ["english", "math", "science"],
        "class": ["V"],
        "name": ["Surya"],
    },
    "id1": {
        "subject_integration": ["english", "math", "science"],
        "class": ["V"],
        "name": ["Sara"],
    },
}


def one_eight(data: dict):
    """Write a Python program to check if a dictionary is empty or not."""
    return not data


print(one_eight({}))
assert one_eight({}) is True
assert one_eight({"a": "b"}) is False


def one_nine(one: dict[Hashable, float], two: dict[Hashable, float]):
    """
    Write a Python program to combine two dictionary adding values for common keys.
    """
    output = one
    for key in two:
        if key in output:
            output[key] += two[key]
        else:
            output[key] = two[key]
    return output


print(one_nine({"a": 100, "b": 200, "c": 300}, {"a": 300, "b": 200, "d": 400}))
assert one_nine({"a": 100, "b": 200, "c": 300}, {"a": 300, "b": 200, "d": 400}) == {
    "b": 400,
    "d": 400,
    "a": 400,
    "c": 300,
}


def two_zero(data: dict):
    """Write a Python program to print all distinct values in a dictionary."""
    return set(data.values())


print(
    two_zero({
        "I": "S001",
        "II": "S002",
        "III": "S001",
        "IV": "S005",
        "V": "S005",
        "VI": "S009",
        "VII": "S007",
    })
)
assert two_zero({
    "I": "S001",
    "II": "S002",
    "III": "S001",
    "IV": "S005",
    "V": "S005",
    "VI": "S009",
    "VII": "S007",
}) == {"S009", "S002", "S007", "S005", "S001"}
