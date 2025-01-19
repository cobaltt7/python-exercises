# 120
string = input("string:")
print(string[:5])


# 121
def isDefined(variable):
    if variable in locals():
        return "local"
    elif variable in globals():
        return "global"
    else:
        return False


print(
    "isDefined",
    isDefined("isDefined") or "undefined",
    isDefined if isDefined("isDefined") else None,
)
print(
    "__name__",
    isDefined("__name__") or "undefined",
    __name__ if isDefined("__name__") else None,
)
print("foo", isDefined("foo") or "undefined", foo if isDefined("foo") else None)
print(locals(), globals())

# 122
n = 20
d = {"x": 200}

print(type(n)())
print(type(d)())

# 123
import sys

print("float_info:", sys.float_info)
print("int_info:", sys.int_info)
print("maxsize:", sys.maxsize)

# 124
print(2 == 2 == 2)

# 125
from functools import reduce

numbers = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
print(reduce(lambda acc, x: acc + x, numbers))

# 126
from inspect import getmodule

print(getmodule(getmodule))

# 127
print(int(input("number:")).bit_length())

# 128
from re import search

result = search(r"[a-z]", input("text:"))
print(not result)

# 129
print(input("string:").rjust(8, "0"))
