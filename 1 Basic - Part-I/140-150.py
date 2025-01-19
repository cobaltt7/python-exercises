# 140
print(bin(int(input("number:"))))

# 141
print(hex(int(input("number:"))))

# 142
import re


def fun(str):
    regex = r"0+|1+"
    matches = re.findall(regex, str)
    if not len(matches) % 2 == 0:
        return False

    for i in range(int(len(matches) / 2)):
        if not len(matches[i * 2]) == len(matches[i * 2 + 1]):
            return False
        if not re.match(r"^0+$", matches[i * 2]):
            return False
        if not re.match(r"^1+$", matches[i * 2 + 1]):
            return False
    return True


print(fun(input("string:")))

# 143
from struct import calcsize

print(calcsize("P") * 8)

# 144
number = 5
string = "abc"
print(type(string))
print(type(number) == int)

# 145
print(type([1]) == list)
print(type(()) == tuple)
print(type({1}) == set)

# 146
from math import __file__

print(__file__)

# 147
a = float(input("number:"))
b = float(input("number:"))
print(a % b == 0)

# 148
list = [42, 17, 88, 53, 29]

min = list[0]
max = list[0]
for number in list:
    if number < min:
        min = number
    if number > max:
        max = number

print({"min": min, "max": max})

# 149
number = int(input("number:"))

sum = 0
for i in range(number):
    sum += i**3

print(sum)


# 150
def fun2(array):
    length = len(array)
    for i in range(length):
        for j in range(i + 1, length):
            if (array[i] * array[j]) % 2:
                return True

    return False


print(fun2([2, 4, 6, 8]))
print(fun2([1, 6, 4, 7, 8]))
print(fun2([1, 3, 5, 7, 9]))
