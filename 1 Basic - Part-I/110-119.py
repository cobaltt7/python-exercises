# 110
numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
print(list(filter(lambda x: x % 15 == 0, numbers)))

# 111
from glob import glob

print(glob(input("glob:")))

# 112
numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
print(numbers)
numbers = numbers[1::]
print(numbers)

# 113
number = input("number:")
if not number.isnumeric():
    raise TypeError("Number please")

# 114
numbers = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
print(list(filter(lambda x: x >= 0, numbers)))

# 115
from functools import reduce

numbers = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
print(reduce(lambda acc, x: acc + x, numbers))

# 116
print("\u0103")

# 117
a = "hi"
b = a
print(id(a) == id(b))
print(a, b)

# 118
bytes = [2, 3, 5, 7]
print(bytearray(bytes))

# 119
from math import trunc

number = float(input("number:"))
print(round(number, 1))
