from re import split


# 7
def eSeven(data):
    for number in data:
        if not number == 1:
            return False
    return True


assert eSeven([0, 1, 2, 3, 4, 5]) is False
assert eSeven([1, 1, 1, 1, 1, 1]) is True
assert eSeven([2, 2, 2, 2, 2]) is False


# 8
def eEight(data):
    items = split(r"(?=[ ,])|(?<=[ ,])", data)

    words = []
    separators = []
    last_sep = False

    for item in items:
        if item == "," or item == " ":
            if last_sep:
                separators[-1] = separators[-1] + item
            else:
                separators.append(item)
            last_sep = True
        else:
            words.append(item)
            last_sep = False

    return [words, separators]


assert eEight("W3resource Python, Exercises.") == [
    ["W3resource", "Python", "Exercises."],
    [" ", ", "],
]
assert eEight("The dance, held in the school gym, ended at midnight.") == [
    ["The", "dance", "held", "in", "the", "school", "gym", "ended", "at", "midnight."],
    [" ", ", ", " ", " ", " ", " ", ", ", " ", " "],
]
assert eEight("The colors in my studyroom are blue, green, and yellow.") == [
    [
        "The",
        "colors",
        "in",
        "my",
        "studyroom",
        "are",
        "blue",
        "green",
        "and",
        "yellow.",
    ],
    [" ", " ", " ", " ", " ", " ", ", ", ", ", " "],
]


# 9
def eNine(data):
    prev = None
    for number in data[:20]:
        if number == prev:
            return False
        prev = number
    return len(set(data)) == 4


assert eNine([1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) is True
assert eNine([1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]) is False
assert eNine([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) is False
