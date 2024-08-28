def eighty_one(string: str, substring: str):
    """
    Write a Python program to find the index of a given string at which a given
    substring starts.
    """
    return string.index(substring) if substring in string else None


print(eighty_one("Python Exercises", "Ex"))
assert eighty_one("Python Exercises", "Ex") == 7
assert eighty_one("Python Exercises", "yt") == 1
assert eighty_one("Python Exercises", "PY") is None


def eighty_two(string: str, width: int):
    """
    Write a Python program to wrap a given string into a paragraph of given width.
    """
    words = string.split()
    lines = []
    line = ""
    for word in words:
        updated = (line + " " + word) if line else word
        if len(updated) > width:
            lines.append(line)
            line = word
        else:
            line = updated
    lines.append(line)
    return "\n".join(lines)


print(eighty_two("The quick brown fox.", 10))
assert eighty_two("The quick brown fox.", 10) == "The quick\nbrown fox."


def eighty_three(number: int):
    """
    Write a Python program to print four values decimal, octal, hexadecimal
    (capitalized), binary in a single line of a given integer.
    """
    return (f"{number}", f"{number:o}", f"{number:X}", f"{number:b}")


print(eighty_three(100))
assert eighty_three(100) == ("100", "144", "64", "1100100")
assert eighty_three(10) == ("10", "12", "A", "1010")
assert eighty_three(25) == ("25", "31", "19", "11001")


def eighty_four(string: str):
    """Write a Python program to swap cases of a given string."""
    out = ""
    for char in string:
        out += char.lower() if char.isupper() else char.upper()
    return out


print(eighty_four("Python Exercises"))
assert eighty_four("Python Exercises") == "pYTHON eXERCISES"
assert eighty_four("Java") == "jAVA"
assert eighty_four("NumPy") == "nUMpY"


def eighty_five(bytes: list[int]):
    """Write a Python program to convert a given Bytearray to Hexadecimal string."""
    return "".join(f"{byte:02X}" for byte in bytes)


print(eighty_five([111, 12, 45, 67, 109]))
assert eighty_five([111, 12, 45, 67, 109]) == "6F0C2D436D"


def eighty_six(string: str, character: str):
    """
    Write a Python program to delete all occurrences of a specified character in a
    given string.
    """
    return "".join(found for found in string if found != character)


print(
    eighty_six("Delete all occurrences of a specified character in a given string", "a")
)
assert (
    eighty_six("Delete all occurrences of a specified character in a given string", "a")
    == "Delete ll occurrences of  specified chrcter in  given string"
)
