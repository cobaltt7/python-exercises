# 78
from sys import builtin_module_names

print(builtin_module_names)

# 79
import sys

print(sys.getsizeof(sys))

# 80
from sys import getrecursionlimit

print(getrecursionlimit())

# 81
num = int(input("number:"))
acc = ""

for i in range(num):
    acc += input("string:")

print(acc)

# 82
numbers = {"one": 1, "two": 2, "three": 3}.values()  # {1, 2, 3} # [1, 2, 3] # (1, 2, 3)
acc = 0

for number in numbers:
    acc += number

print(acc)

# 83
numbers = [-3, -2, -1, 1, 2, 3]
number = float(input("number:"))
print(not bool(len([x for x in numbers if x <= number])))

# 84
string = input("string:")
character = input("character:")[0]
print(len([x for x in string if x == character]))

# 85
from os import path

print("is file?", path.isfile(input("path:")))

# 86
print([ord(character) for character in input("string:")])

# 87
from os import path

print(path.getsize(input("file:")))

# 88
x = float(input("number:"))
y = float(input("number:"))
print(f"{x}+{y}={x + y}")
