# 12
def eTwelve(data):
    return list(map(lambda word: word == word[::-1], data))


assert eTwelve(["palindrome", "madamimadam", "", "foo", "eyes"]) == [
    False,
    True,
    True,
    False,
    False,
]


# 13
def eThirteen(data):
    return list(filter(lambda word: word.startswith(data[0]), data[1]))


assert eThirteen(("ca", ("cat", "car", "fear", "center"))) == ["cat", "car"]
assert eThirteen(("do", ("cat", "dog", "shatter", "donut", "at", "todo"))) == [
    "dog",
    "donut",
]


# 14
def eFourteen(data):
    return list(map(len, data))


assert eFourteen(["cat", "car", "fear", "center"]) == [3, 3, 4, 6]
assert eFourteen(["cat", "dog", "shatter", "donut", "at", "todo", ""]) == [
    3,
    3,
    7,
    5,
    2,
    4,
    0,
]


# 15
def eFifteen(data):
    longest = ""
    for word in data:
        if len(word) > len(longest):
            longest = word
    return longest


assert eFifteen(["cat", "car", "fear", "center"]) == "center"
assert eFifteen(["cat", "dog", "shatter", "donut", "at", "todo", ""]) == "shatter"
