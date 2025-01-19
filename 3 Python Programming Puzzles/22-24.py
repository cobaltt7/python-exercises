# 22
def eTwentyTwo(data):
    sum = 0
    for char in data:
        if char.isupper():
            sum += ord(char)
    return sum


assert eTwentyTwo("PytHon ExerciSEs") == 373
assert eTwentyTwo("JavaScript") == 157


# 23
def eTwentyThree(seq):
    drops = []
    for index in range(len(seq)):
        if seq[index] < seq[index - 1]:
            drops.append(index)
    return drops


assert eTwentyThree(
    [0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]
) == [1, 4, 6, 8, 10, 11, 15, 16, 18]
assert eTwentyThree([6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert eTwentyThree([1, 19, 5, 15, 5, 25, 5]) == [0, 2, 4, 6]


# 24
def eTwentyFour(data):
    return list(map(lambda index: max(data[: index + 1]), range(len(data))))


assert eTwentyFour(
    [0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]
) == [0, 0, 3, 8, 8, 9, 9, 14, 14, 14, 14, 14, 14, 17, 41, 41, 41, 41, 41, 41]
assert eTwentyFour([6, 5, 4, 3, 2, 1]) == [6, 6, 6, 6, 6, 6]
assert eTwentyFour([1, 19, 5, 15, 5, 25, 5]) == [1, 19, 19, 19, 19, 25, 25]
