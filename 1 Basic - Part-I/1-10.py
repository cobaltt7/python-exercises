# 1
print(
    "Twinkle, twinkle, little star,\n"
    + "\tHow I wonder what you are!\n"
    + "\t\tUp above the world so high,\n"
    + "\t\tLike a diamond in the sky.\n"
    + "Twinkle, twinkle, little star,\n"
    + "How I wonder what you are"
)

# 2
from datetime import datetime

print(datetime.now())

# 2
import sys

print(sys.version)

# 3
import math

radius = float(input("Radius:"))
print(f"r = {radius}")
print(f"Area = {math.pi * radius ** 2}")

# 4
first_name = input("First name:")
last_name = input("Last name:")
print(f"{last_name}, {first_name}")

# 5
first_name = input("First name:")
last_name = input("Last name:")
print(f"{last_name}, {first_name}")

# 6
numbers = input("Numbers:").split(", ")
print(numbers)
print(tuple(numbers))

# 7
extension = input("Filename:").split(".")[1]
print(extension)

# 8
color_list = ["Red", "Green", "White", "Black"]
print(color_list[0])
print(color_list[-1])

# 9
exam_st_date = (11, 12, 2014)
print(
    "The examination will start on"
    f" {exam_st_date[2]}-{exam_st_date[0]}-{exam_st_date[1]}"
)

# 10
n = int(input("n:"))
n2 = (n * 10) + n
print(n + n2 + (n * 100 + n2))
