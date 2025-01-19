# 55
a1, a2, b1, b2, c1, c2, d1, d2 = map(float, input("numbers:").split())

slopeCD = (d2 - c2) / (d1 - c1)
slopeAB = (b2 - a2) / (b1 - a1)
print(slopeAB * slopeCD == -1)

# 56
from re import findall
from functools import reduce

line = input("characters:")
print(reduce(lambda acc, number: acc + int(number), findall(r"\d+", line), 0))

# 58
from re import sub

string = input("string:")
print(sub(r"#(\d)(.)", lambda match: match.group(2) * int(match.group(1)), string))

# 59
from functools import reduce

sideCount = int(input("points:"))

sides = []
for side in range(sideCount):
    sides.append(tuple(map(float, input("coordinates:").split())))


def mutiplyXY(acc, entry):
    index, curr = entry
    if index + 1 == len(sides):
        return acc
    return acc + curr[0] * sides[index + 1][1]


def mutiplyYX(acc, entry):
    index, curr = entry
    if index + 1 == len(sides):
        return acc
    return acc + curr[1] * sides[index + 1][0]


entries = list(enumerate(sides))
print((reduce(mutiplyXY, entries, 0) - reduce(mutiplyYX, entries, 0)) / 2)
