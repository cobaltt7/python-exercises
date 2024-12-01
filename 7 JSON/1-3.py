import json
from typing import Any


def one(json_data: str):
    """Write a Python program to convert JSON data to Python object"""
    return json.loads(json_data)


print(one('{"hi":102}'))
assert one('{"hi":102}') == {"hi": 102}
assert one('{"Name": "David", "Class": "I", "Age": 6}') == {
    "Name": "David",
    "Class": "I",
    "Age": 6,
}


def two(data: Any):
    """Write a Python program to convert Python object to JSON data."""
    return json.dumps(data)


print(two({"hi": 102}))
assert two({"hi": 102}) == '{"hi": 102}'
assert (
    two({"Name": "David", "Class": "I", "Age": 6})
    == '{"Name": "David", "Class": "I", "Age": 6}'
)


def three(data: list[Any]):
    """Write a Python program to convert Python objects into JSON strings. Print all the values."""
    return list(map(json.dumps, data))


print(
    three([
        {"name": "David", "age": 6, "class": "I"},
        ["Red", "Green", "Black"],
        "Python Json",
        (1234),
        21.34,
        True,
        False,
        None,
    ])
)
assert three([
    {"name": "David", "age": 6, "class": "I"},
    ["Red", "Green", "Black"],
    "Python Json",
    (1234),
    21.34,
    True,
    False,
    None,
]) == [
    '{"name": "David", "age": 6, "class": "I"}',
    '["Red", "Green", "Black"]',
    '"Python Json"',
    "1234",
    "21.34",
    "true",
    "false",
    "null",
]
