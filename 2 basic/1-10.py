# 1
numbers = input("numbers:")
print(len(set([*numbers])) == len(numbers))

# 2
from random import shuffle

chars = ["a", "e", "i", "o", "u"]
shuffle(chars)
print("".join(chars))

# 3
list = [
    *"`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,."
    " ~!@#$%^&*()_+QWERTYUP{}|ASDFGHJKL:\"'ZXCVBNM<>?"
]

while len(list) > 2:
    print(list[2])
    list.pop(2)

# 4
numbers = [1, -6, 4, 2, -1, 2, 0, -2, 0]

unique = list(set(numbers))
length = len(unique)
for idx, i in enumerate(unique):
    for jdx, j in enumerate(unique[idx + 1 :]):
        for k in unique[jdx + 1 :]:
            if (i + j + k) == 0:
                print((i, j, k))

# 5
for num in range(1000):
    print(str(num).zfill(3))

# 6
text = input("text:")
words = text.split()
counts = {}
for word in words:
    if not word in counts:
        counts[word] = 0

    counts[word] += 1
print(counts)

# 7
text = input("text:")
chars = [*text]
counts = {}
for char in chars:
    if not char in counts:
        counts[char] = 0

    counts[char] += 1
print(counts)

# 8
from requests import get
from xml.etree import ElementTree

response = get("https://news.google.com/rss")
root = ElementTree.fromstring(response.text)
for tag in root.findall("channel/item/title"):
    print(tag.text)

# 9
from pkgutil import iter_modules

print(list(map(lambda module: module.name, iter_modules())))

# 10
from platform import platform

print(platform())
