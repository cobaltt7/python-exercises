# 113
print(
    " ".join(
        map(
            lambda word: word if len(word) % 2 else "".join(reversed(word)),
            input("string:").split(),
        )
    )
)

# 114
starting = ord(input("character:"))
ending = ord(input("character:"))
print(list(map(chr, range(starting, ending + 1))))

# 115
starting = input("number:")
ending = input("number:")
print(range(int(starting), int(ending)))

# 116
from math import floor


def isPrime(number):
    if number < 2:
        return False
    for i in range(2, floor(number / 2) + 1):
        if number % i == 0:
            return False
    return True


for i in range(int(input("number:")), int(input("number:")) + 1):
    if not isPrime(i):
        print(i)

# 117
from requests import get

response = get("https://example.com")
print(response)
print()
print(response.text)

# 118
import os

print(__name__)
print(os.getppid())
print(os.getpid())
