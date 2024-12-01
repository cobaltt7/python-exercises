def eTwentyEight(data):
    """
    Write a Python program to select a string from a given list of strings with the most unique
    characters.
    """
    max = 0
    found = ""

    for word in data:
        count = len(set(word))
        if count > max:
            max = count
            found = word

    return found


def eTwentyNine(data):
    """
    Write a Python program to find the indices of two numbers that sum to 0 in a given list of
    numbers.
    """

    for index, number in enumerate(data):
        other = number * -1
        otherIndex = other in data[index + 1 :] and data.index(other, index + 1)
        if otherIndex is not False:
            return [index, otherIndex]


def eThirty(data):
    """
    Write a Python program to find a list of strings that have fewer total characters (including
    repetitions).
    """
    min = None
    found = None

    for array in data:
        length = sum(map(len, array))
        if min is None or length < min:
            min = length
            found = array

    return found


assert (
    eTwentyEight([
        "cat",
        "catatatatctsa",
        "abcdefhijklmnop",
        "124259239185125",
        "",
        "foo",
        "unique",
    ])
    == "abcdefhijklmnop"
)
assert eTwentyEight(["Green", "Red", "Orange", "Yellow", "", "White"]) == "Orange"

assert eTwentyNine([1, -4, 6, 7, 4]) == [1, 4]
assert eTwentyNine([0, 1, 22, 3, 0]) == [0, 4]
assert eTwentyNine([0]) is None
assert eTwentyNine([1232, -20352, 12547, 12440, 741, 341, 525, 20352, 91, 20]) == [1, 7]

assert eThirty(
    [["this", "list", "is", "narrow"], ["I", "am", "shorter but wider"]]
) == ["this", "list", "is", "narrow"]
assert eThirty([["Red", "Black", "Pink"], ["Green", "Red", "White"]]) == [
    "Red",
    "Black",
    "Pink",
]
