# 16
def eSixteen(data):
    return list(filter(lambda word: data[0] in word, data[1]))


assert eSixteen(("ca", ("cat", "car", "fear", "center"))) == ["cat", "car"]
assert eSixteen(("o", ("cat", "dog", "shatter", "donut", "at", "todo", ""))) == [
    "dog",
    "donut",
    "todo",
]
assert eSixteen(("oe", ("cat", "dog", "shatter", "donut", "at", "todo", ""))) == []


# 17
def eSeventeen(data):
    return " ".join(list(map(str, range(data + 1))))


assert eSeventeen(4) == "0 1 2 3 4"
assert eSeventeen(15) == "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15"


# 18
def eEighteen(data):
    matrix, target = data
    filtered = enumerate(
        map(
            lambda row: (filter(lambda entry: entry[1] == target, enumerate(row))),
            matrix,
        )
    )

    indices = []
    for row, items in filtered:
        for column in items:
            indices.append([row, column[0]])

    return indices


assert eEighteen(
    [([1, 3, 2, 32, 19], [19, 2, 48, 19], [], [9, 35, 4], [3, 19]), 19]
) == [[0, 4], [1, 0], [1, 3], [4, 1]]

assert eEighteen([([1, 2, 3, 2], [], [7, 9, 2, 1, 4]), 2]) == [[0, 1], [0, 3], [2, 2]]
