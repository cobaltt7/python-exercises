def forty(data):
    """
    Write a Python program to find strings that, when case is flipped, give a target where vowels
    are replaced by characters two later.
    """
    shifted = [
        chr(ord(letter) + 2) if letter in "aeiouAEIOU" else letter for letter in data
    ]
    flipped = [
        letter.lower() if letter.isupper() else letter.upper() for letter in shifted
    ]
    return "".join(flipped)


def fortyOne(data):
    """
    Write a Python program to sort numbers based on strings.
    """
    numbers = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    return " ".join(sorted(set(data.split()), key=lambda number: numbers[number]))


assert forty("Python") == "pYTHQN"
assert forty("aeiou") == "CGKQW"
assert forty("Hello, world!") == "hGLLQ, WQRLD!"
assert forty("AEIOU") == "cgkqw"

assert fortyOne("six one four one two three") == "one two three four six"
assert (
    fortyOne("six one four three two nine eight") == "one two three four six eight nine"
)
assert (
    fortyOne("nine eight seven six five four three two one")
    == "one two three four five six seven eight nine"
)
