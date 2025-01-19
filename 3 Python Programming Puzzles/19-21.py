# 19
def eNineteen(data):
    return data.split(" " if " " in data else ",")


assert eNineteen("a b c d") == ["a", "b", "c", "d"]
assert eNineteen("a,b,c,d") == ["a", "b", "c", "d"]
assert eNineteen("abcd") == ["abcd"]


# 20
def eTwenty(seq):
    diff = seq[1] - seq[0]
    prev = seq[0]

    if diff == 0:
        return None

    for number in seq[1:]:
        if prev + diff != number:
            return None
        prev = number

    return "Increasing" if diff > 0 else "Decreasing"


assert eTwenty([1, 2, 3, 4, 5, 6]) == "Increasing"
assert eTwenty([6, 5, 4, 3, 2, 1]) == "Decreasing"
assert eTwenty([19, 19, 5, 5, 5, 5, 5]) is None


# 21
def eTwentyOne(data):
    return list(
        map(
            lambda word: any(map(lambda letter: len(letter) == 1, word.split(" "))),
            data,
        )
    )


assert eTwentyOne(["cat", "car", "fear", "center"]) == [False, False, False, False]
assert eTwentyOne(["ca t", "car", "fea r", "cente r"]) == [True, False, True, True]
