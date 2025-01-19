# 65
from math import floor

seconds = float(input("seconds:"))
days = floor(seconds / 86400)
dayHours = days * 24
hours = floor(seconds / 3600) - dayHours
hourMinutes = (hours + dayHours) * 60
minutes = floor(seconds / 60) - hourMinutes
print(f"{days} days, {hours}:{minutes}:{seconds - (minutes + hourMinutes) * 60}")

# 66
print(703 * float(input("weight (lb):")) / ((float(input("height (ft):")) * 12) ** 2))

# 67
kilopascals = float(input("kilopascals:"))
print("lb/in²:", kilopascals / 6.895)
print("mmHg:", kilopascals * 7.501)
print("atm:", kilopascals / 101.3)

# 68
number = input("number:")

sum = 0
for digit in number:
    sum += int(digit)

print(sum)

# 69
numbers = [float(input("number:")), float(input("number:")), float(input("number:"))]
numbers.sort()
print(numbers)

# 70
import os

print(sorted(os.listdir(), key=os.path.getmtime))

# 71
import os

print(sorted(os.listdir(), key=os.path.getmtime))

# 72
import math

print(math.__doc__)

# 73
x1 = float(input("x1:"))
y1 = float(input("y1:"))
x2 = float(input("x2:"))
y2 = float(input("y2:"))
print(f"({x2 + (x1 - x2) / 2}, {y2 + (y1 - y2) / 2})")

# 74
from hashlib import sha1

result = sha1(input("string:").encode())
print(result.hexdigest())

# 75
from sys import copyright

print(copyright)

# 76
from sys import argv

print(argv)

# 77
from sys import byteorder

print(f"{byteorder}-endian")
