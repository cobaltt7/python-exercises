# 68
from math import floor


def isPrime(number):
    if number < 2:
        return False
    for i in range(2, floor(number / 2) + 1):
        if number % i == 0:
            return False
    return True


count = 0
for i in range(int(input("number:"))):
    if isPrime(i + 1):
        print(i + 1)
        count += 1

print(count)


# 69
word1 = input("word:")
word2 = input("word:")

charCount = len(word2)
isomorphic = len(word1) == charCount

if isomorphic:
    chars1 = list(map(word1.index, word1))
    chars2 = list(map(word2.index, word2))
    for index in range(charCount):
        if chars1[index] != chars2[index]:
            isomorphic = False
            break

print(isomorphic)

# 70
strings = ("abcdefgh", "abcefgh")
# strings = ("w3r", "w3resource")
# strings = ("Python", "PHP", "Perl")
# strings = ("Python", "PHP", "Java")

sorted_strings = sorted(strings, key=len)
prefix = ""

for index, letter in enumerate(sorted_strings[0]):
    matches = True
    for word in sorted_strings[1:]:
        if word[index] != letter:
            matches = False
    if matches:
        prefix += letter
    else:
        break

print(prefix)

# 71
VOWELS = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
word = input("word:")
vowels = list(filter(lambda char: char in VOWELS, word))
new_chars = map(
    lambda item: vowels.pop() if item[1] in VOWELS else item[1], enumerate(word)
)
print("".join(new_chars))
