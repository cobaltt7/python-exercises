# 48
count = 0
while True:
    digit, sum = map(int, input().split())
    if digit == 0 and sum == 0:
        break
    for i in range(10):
        if digit + i == sum:
            count += 1

print(count)

# 49
from math import sqrt

horizontal, vertical, diagonal = map(int, input("sides:").split(","))
if sqrt(horizontal**2 + vertical**2) == diagonal:
    print("rectangle")
else:
    print("not rectangle")

# 50
words = input("string:").split("Python")
print("Java".join(map(lambda segment: segment.replace("Java", "Python"), words)))

# 51
number = input("number:")
print(int("".join(sorted(number, reverse=True))) - int("".join(sorted(number))))

# 52
from math import floor


def isPrime(number):
    if number < 2:
        return False
    for i in range(2, floor(number / 2) + 1):
        if number % i == 0:
            return False
    return True


count = 0
number = int(input("number:"))
i = 1
sum = 0
while count < number:
    if isPrime(i):
        sum += i
        count += 1
    i += 1

print(sum)

# 53
from math import floor


def isPrime2(number):
    if number < 2:
        return False
    for i in range(2, floor(number / 2) + 1):
        if number % i == 0:
            return False
    return True


number = int(input("number:"))

count = 0
for i in range(floor(number / 2)):
    if not (isPrime2(i) and isPrime2(number - i)):
        continue
    count += 1

print(count)

# 54
number = int(input("number:"))
print((number * number + number + 2) // 2)
