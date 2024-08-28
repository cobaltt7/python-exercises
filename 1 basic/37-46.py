# 37
name = input("name:")
age = input("age:")
address = input("address:")

print(name)
print(age)
print(address)

# 38
x = float(input("x:"))
y = float(input("y:"))
print((x + y) ** 2)

# 39
amount = float(input("amount:"))
interest = float(input("interest:")) / 100
years = int(input("years:"))

sum = amount
for i in range(years):
    sum += interest * sum

print(round(sum, 2))

# 40
from math import sqrt

x1 = float(input("x1:"))
x2 = float(input("x2:"))
y1 = float(input("y1:"))
y2 = float(input("y2:"))

x = x1 - y1
y = x2 - y2

print(sqrt((x**2) + (y**2)))

# 41
from os import path

print(path.exists(input("file:")))

# 42
from sys import maxsize

print(maxsize > 2**32)

# 43
from os import name
from platform import system, release

print(system(), name, release())

# 44
from sysconfig import get_paths

print(get_paths()["purelib"])

# 45
from subprocess import call

call(["ls", "-l"])

# 46
print(__file__)
