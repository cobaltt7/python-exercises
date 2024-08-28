def eighty_seven(one: str, two: str):
    """
    Write a Python program find the common values that appear in two given strings.
    """
    three = one + two
    return "".join(sorted(set(one).intersection(two), key=three.index))


print(eighty_seven("Python3", "Python2.7"))
assert eighty_seven("Python3", "Python2.7") == "Python"


def eighty_eight(string: str, min_len: int):
    """
    Write a Python program to check whether a given string contains a capital letter, a
    lower case letter, a number and a minimum length.
    """
    if len(string) < min_len:
        return False

    upper = False
    lower = False
    number = False
    for character in string:
        if character.isupper():
            upper = True
        elif character.islower():
            lower = True
        elif character.isnumeric():
            number = True
        if upper and lower and number:
            return True
    return False


print(eighty_eight("W3resource", 8))
assert eighty_eight("W3resource", 8) == True


def eighty_nine(string: str, characters: list[str]):
    """Write a Python program to remove unwanted characters from a given string."""
    return "".join(found for found in string if found not in characters)


print(eighty_nine("Pyth*^on Exercis^es", ["#", "*", "!", "^", "%"]))
assert (
    eighty_nine("Pyth*^on Exercis^es", ["#", "*", "!", "^", "%"]) == "Python Exercises"
)
assert eighty_nine("A%^!B#*CD", ["#", "*", "!", "^", "%"]) == "ABCD"
