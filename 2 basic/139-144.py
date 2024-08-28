# 139
number = int(input("number:"))

small = number
big = number + 1

while True:
    if str(small) == str(small)[::-1]:
        print(small)
        break
    if str(big) == str(big)[::-1]:
        print(big)
        break
    small -= 1
    big += 1

# 140
numbers = [
    "0.49",
    "0.54",
    "0.54",
    "0.54",
    "0.54",
    "0.54",
    "0.55",
    "0.54",
    "0.54",
    "0.54",
    "0.55",
    "0.55",
    "0.55",
    "0.54",
    "0.55",
    "0.55",
    "0.54",
    "0.55",
    "0.55",
    "0.54",
]
print(list(map(float, numbers)))

# 141
from socket import gethostbyaddr

result = gethostbyaddr(input("input:"))
print(result[0])

# 142
string = input("string:")

zeros = 0
ones = 0

for digit in string:
    if digit == "0":
        if ones != 0:
            if zeros != ones:
                break
            zeros = 0
            ones = 0
        zeros += 1
    elif digit == "1":
        ones += 1

print(zeros == ones)

# 143
print("\N{SNOWMAN}")

# 144
print(str(3.5))
