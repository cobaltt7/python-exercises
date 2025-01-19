# 26
from matplotlib import pyplot

pyplot.hist(
    [1, 2, 3, 56, 3, 8, 89, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 2, 1, 2, 3, 4, 5, 64, 56, 8]
)
pyplot.show()

# 27
list = [
    1,
    2,
    3,
    56,
    3,
    8,
    89,
    9,
    0,
    9,
    8,
    7,
    6,
    5,
    4,
    3,
    2,
    2,
    1,
    2,
    3,
    4,
    5,
    64,
    56,
    8,
]
print("".join(str(num) for num in list))

# 28
list = [
    386,
    462,
    47,
    418,
    907,
    344,
    236,
    375,
    823,
    566,
    597,
    978,
    328,
    615,
    953,
    345,
    399,
    162,
    758,
    219,
    918,
    237,
    412,
    566,
    826,
    248,
    866,
    950,
    626,
    949,
    687,
    217,
    815,
    67,
    104,
    58,
    512,
    24,
    892,
    894,
    767,
    553,
    81,
    379,
    843,
    831,
    445,
    742,
    717,
    958,
    743,
    527,
]
for number in list:
    if number % 2 == 0:
        print(number)
    if number == 237:
        break

# 29
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(set(color for color in color_list_1 if color not in color_list_2))

# 30
height = float(input("height:"))
base = float(input("base:"))
print((height * base) / 2)

# 31
a = int(input("a:"))
b = int(input("b:"))


def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(a, b))

# 32
a = int(input("a:"))
b = int(input("b:"))


def gcd2(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    return gcd2(b, a % b)


print((a * b) / gcd2(a, b))

# 33
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

print(0 if a == b or b == c or a == c else a + b + c)

# 34
a = int(input("a:"))
b = int(input("b:"))
sum = a + b
print(20 if 15 <= sum <= 20 else a + b)

# 35
a = int(input("a:"))
b = int(input("b:"))

print(a == b or a + b == 5 or abs(a - b) == 5)

# 36
a = input("a:")
b = input("b:")

if a.isnumeric() and b.isnumeric():
    intA = float(a)
    intB = float(b)
    if intA.is_integer() and intB.is_integer():
        print(intA + intB)
