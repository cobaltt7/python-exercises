from difflib import SequenceMatcher
from re import split


def ninety_five(red: int, green: int, blue: int):
    """
    Write a Python program to convert the values of RGB components to a hexadecimal
    color code.
    """
    return f"#{red:02X}{green:02X}{blue:02X}"


print(ninety_five(255, 165, 1))
assert ninety_five(255, 165, 1) == "#FFA501"
assert ninety_five(255, 255, 255) == "#FFFFFF"
assert ninety_five(0, 0, 0) == "#000000"
assert ninety_five(0, 0, 128) == "#000080"
assert ninety_five(192, 192, 192) == "#C0C0C0"


def ninety_six(string: str):
    """Write a Python program to convert a given string to camelcase."""
    words = split(r"[\s_-]+|(?<=[a-z])(?=[A-Z])", string)
    words = list(filter(bool, words))
    first = words.pop(0).lower()
    return first + "".join(map(lambda word: word[0].upper() + word[1:].lower(), words))


print(ninety_six("Write a Python program to convert a given string to camelcase."))
assert (
    ninety_six("Write a Python program to convert a given string to camelcase.")
    == "writeAPythonProgramToConvertAGivenStringToCamelcase."
)
assert ninety_six("JavaScript") == "javaScript"
assert ninety_six("Foo-Bar") == "fooBar"
assert ninety_six("foo_bar") == "fooBar"
assert ninety_six("--foo.bar") == "foo.bar"
assert ninety_six("Foo-BAR") == "fooBar"
assert ninety_six("fooBAR") == "fooBar"
assert ninety_six("foo bar") == "fooBar"


def ninety_seven(string: str):
    """Write a Python program to convert a given string to snake case."""
    words = split(r"[\s_-]+|(?<=[a-z])(?=[A-Z])", string)
    words = list(filter(bool, words))
    return "_".join(words).lower()


print(ninety_seven("Write a Python program to convert a given string to snake case."))
assert (
    ninety_seven("Write a Python program to convert a given string to snake case.")
    == "write_a_python_program_to_convert_a_given_string_to_snake_case."
)
assert ninety_seven("JavaScript") == "java_script"
assert ninety_seven("Foo-Bar") == "foo_bar"
assert ninety_seven("foo_bar") == "foo_bar"
assert ninety_seven("--foo.bar") == "foo.bar"
assert ninety_seven("Foo-BAR") == "foo_bar"
assert ninety_seven("fooBAR") == "foo_bar"
assert ninety_seven("foo bar") == "foo_bar"


def ninety_eight(string: str):
    """Write a Python program to decapitalize the first letter of a given string."""
    return string[0].lower() + string[1:]


print(ninety_eight("Java Script"))
assert ninety_eight("Java Script") == "java Script"
assert ninety_eight("Python") == "python"


def ninety_nine(string: str):
    """
    Write a Python program to split a given multiline string into a list of lines.
    """
    return string.split("\n")


print(ninety_nine("This\nis a\nmultiline\nstring.\n"))
assert ninety_nine("This\nis a\nmultiline\nstring.\n") == [
    "This",
    "is a",
    "multiline",
    "string.",
    "",
]
