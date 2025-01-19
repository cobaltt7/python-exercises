# 89
day = int(input("day:"))
if day == 1:
    print("First day of a Month!")

# 90
from shutil import copy2

copy2(__file__, "main-copy.py")

# 91
a = 2
b = 1
print({"a": a, "b": b})

oldB = b
b = a
a = oldB
print({"a": a, "b": b})

# 92
print('\r\n\t\f"\\')

# 93
b = "hello"
print({"type": type(b), "idenity": id(b), "value": b})

# 94
print(list(bytes(input("bytes:"), "utf8")))

# 95
print(input("string:").isnumeric())

# 96
from traceback import format_stack

print("".join(format_stack()))

# 97
print(set(globals()))

# 98
from time import strftime

print(strftime("%H:%M:%S"))

# 99
from time import sleep

print("spam")
print("spam")
print("spam")
print("spam")
print("spam")
print("spam")
print("spam")
sleep(0.5)
print("\033[H\033[J", end="")
print("spam")
print("spam")
