# 11
print(help(abs))

# 12
from calendar import month

print(month(2007, 12))

# 13
print(
    """
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example"""
)

# 14
from datetime import date

print(date(2014, 7, 11) - date(2014, 7, 2))

# 15
from math import pi

print(4 / 3 * pi * (float(input("radius:")) ** 3))

# 16
num = float(input("number:"))
if num > 17:
    print((num - 17) * 2)
else:
    print(17 - num)

# 17
num = float(input("number:"))
print(900 <= num <= 1100 or 1900 <= num <= 2100)

# 18
num1 = float(input("number:"))
num2 = float(input("number:"))
num3 = float(input("number:"))
if num1 == num2 and num1 == num3:
    print(num1 * 9)
else:
    print(num1 + num2 + num3)

# 19
string = input("string:")
if not string.startswith("Is "):
    string = "Is " + string
print(string)

# 20
num = int(input("number:"))
string = input("string:")
print(string * num)

# 21
num = int(input("number:"))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 22
list = [1, 2, 4, 3, 4, 5, 4, 6]
print(list.count(4))

# 23
string = input("string:")
number = int(input("number:"))
print(string[:2] * number)

# 24
vowels = ("a", "e", "i", "o", "u")
letter = input("Is _ a vowel?").lower()
if letter in vowels:
    print("Yes")
elif letter == "y":
    print("Sometimes")
else:
    print("No")

# 25
values = [1, 5, 8, 3]
number = int(input("Number:"))
print(number in values)
