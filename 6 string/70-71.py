def seventy(one: str, two: str):
    """
    Write a Python program to create a string from two given strings concatenating
    uncommon characters of the said strings.
    """
    result = sorted(set(one.lower()).symmetric_difference(two.lower()))
    return "".join(result)


print(seventy("abcdpqr", "xyzabcd"))
assert seventy("abcdpqr", "xyzabcd") == "pqrxyz"


def seventy_one(string: str):
    """
    Write a Python program to move all spaces to the front of a given string in single
    traversal.
    """
    spaces = 0
    out = ""
    for character in string:
        if character == " ":
            spaces += 1
        else:
            out += character
    return (" " * spaces) + out


print(seventy_one("Python Exercises"))
assert seventy_one("Python Exercises") == " PythonExercises"
