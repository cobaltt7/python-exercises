import json
from typing import Any


def four(json_data: Any):
    """
    Write a Python program to convert Python dictionary object (sort by key) to JSON data. Print the
    object members with indent level 4.
    """
    return json.dumps(json_data, sort_keys=True, indent=4)


print(four({"4": 5, "6": 7, "1": 3, "2": 4}))
assert (
    four({"4": 5, "6": 7, "1": 3, "2": 4})
    == """{
    "1": 3,
    "2": 4,
    "4": 5,
    "6": 7
}"""
)


def five(data: str):
    """Write a Python program to convert JSON encoded data into Python objects."""
    return json.loads(data)


print(five('{"name": "David", "age": 6, "class": "I"}'))
assert five('{"name": "David", "age": 6, "class": "I"}') == {
    "name": "David",
    "age": 6,
    "class": "I",
}
assert five('["Red", "Green", "Black"]') == ["Red", "Green", "Black"]
assert five('"Python Json"') == "Python Json"
assert five("1234") == 1234
assert five("21.34") == 21.34


def six():
    """Write a Python program to create a new JSON file from an existing JSON file."""
    with open("./data.json", "r", encoding="utf8") as file:
        contents = json.load(file)
        contents["hi"] += 1
        with open("./data-new.json", "w", encoding="utf8") as new_file:
            json.dump(contents, new_file)


six()
