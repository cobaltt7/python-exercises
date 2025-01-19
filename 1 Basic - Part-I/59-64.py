# 59
feet = float(input("feet:"))
inches = float(input("inches:"))
print((inches + feet * 12) * 2.54)

# 60
from math import sqrt

a = float(input("a:"))
b = float(input("b:"))
print(sqrt(a**2 + b**2))

# 61
feet = float(input("feet:"))
print("inches:", feet * 12)
print("yards:", feet / 3)
print("miles:", feet / 5_280)

# 62
from re import search

result = search(
    r"^(?:(?P<weeks>\d*(?:.\d+)?)\s*w(?:(?:ee)?ks?)?\s*)?\s*"
    + r"(?:(?P<days>\d*(?:.\d+)?)\s*d(?:ays?)?\s*)?\s*"
    + r"(?:(?P<hours>\d*(?:.\d+)?)\s*h(?:(?:ou)?rs?)?\s*)?\s*"
    + r"(?:(?P<minutes>\d*(?:.\d+)?)\s*m(?:in(?:ute)?s?)?\s*)?\s*"
    + r"(?:(?P<seconds>\d*(?:.\d+)?)\s*s(?:ec(?:ond)?s?)?\s*)?$",
    input("text:"),
)

weeks = float(result and result.group("weeks") or 0)
days = float(result and result.group("days") or 0)
hours = float(result and result.group("hours") or 0)
minutes = float(result and result.group("minutes") or 0)
seconds = float(result and result.group("seconds") or 0)

totalDays = days + 7 * weeks
totalHours = hours + 24 * totalDays
totalMinutes = minutes + 60 * totalHours
totalSeconds = seconds + 60 * totalMinutes

print("seconds:", totalSeconds)

# 63
from os import path

print(path.abspath(input("path:")))

# 64
from os import path
from datetime import date

print(date.fromtimestamp(path.getmtime(input("path:"))))
