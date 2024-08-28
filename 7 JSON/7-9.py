import json
from typing import Any


def seven(data: Any):
    """Write a Python program to check whether an instance is complex or not."""
    return isinstance(data, complex)


print(2 + 3j)
print(seven(2 + 3j))
assert seven(2 + 3j) is True
assert seven(4) is False


def eight(data: str):
    """Write a Python program to check whether a JSON string contains complex object or not."""
    parsed = json.loads(data)
    return "__complex__" in parsed


print(eight('{"__complex__": true, "real": 4, "img": 5}'))
assert eight('{"real": 4, "img": 3}') is False
assert eight('{"__complex__": true, "real": 4, "img": 5}') is True


def nine(data: str):
    """Write a Python program to access only unique key value of a Python object."""
    return json.loads(data)


print(nine('{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'))
assert nine('{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}') == {"a": 4, "b": 2}
