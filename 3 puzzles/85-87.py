def eightyFive(data):
    """
    Write a Python program to find an increasing sequence consisting of the elements of the
    original list.
    """
    return sorted(set(data))


print(eightyFive([9, -2, 3, 4, -2, 0, 2, -3, 8, -1]))
assert eightyFive([1, 3, 79, 10, 4, 2, 39]) == [1, 2, 3, 4, 10, 39, 79]
assert eightyFive([11, 31, 40, 68, 77, 93, 48, 1, 57]) == [
    1,
    11,
    31,
    40,
    48,
    57,
    68,
    77,
    93,
]
assert eightyFive([9, -2, 3, 4, -2, 0, 2, -3, 8, -1]) == [-3, -2, -1, 0, 2, 3, 4, 8, 9]


def eightySix(data):
    """
    Write a Python program to find the vowels from each of the original texts (y counts as a vowel
    at the end of the word) from a given list of strings.
    """

    def extract_vowels(word):
        lastIndex = len(word) - 1
        entries = enumerate(word)
        filtered = filter(
            lambda entry: entry[1]
            in ("aeiouyAEIOUY" if entry[0] == lastIndex else "aeiouAEIOU"),
            entries,
        )
        return "".join(map(lambda entry: entry[1], filtered))

    return list(map(extract_vowels, data))


print(eightySix(["w3resource", "Python", "Java", "C++"]))
assert eightySix(["w3resource", "Python", "Java", "C++"]) == ["eoue", "o", "aa", ""]
assert eightySix(["ably", "abruptly", "abecedary", "apparently", "acknowledgedly"]) == [
    "ay",
    "auy",
    "aeeay",
    "aaey",
    "aoeey",
]


def eightySeven(data):
    """
    Write a Python program to find a valid substring of a given string that contains matching
    brackets, at least one of which is nested.
    """
    data = data.lstrip("]").rstrip("[")
    opened = 0
    string = ""

    for bracket in data:
        if bracket == "]":
            if opened > 0:
                opened -= 1
                string += bracket
        else:
            opened += 1
            string += bracket
        if opened == 0:
            if len(string) > 2:
                return string
            else:
                string = ""
    return eightySeven(data[1:])


print(
    eightySeven(
        "]]]]]]]]]]]]]]]]][][][][]]]]]]]]]]][[[][[][[[[[][][][]][[[[[[[[[[[[[[[[[["
    )
)
assert eightySeven("]][][[]]]") == "[[]]"
assert (
    eightySeven(
        "]]]]]]]]]]]]]]]]][][][][]]]]]]]]]]][[[][[][[[[[][][][]][[[[[[[[[[[[[[[[[["
    )
    == "[[][][][]]"
)
