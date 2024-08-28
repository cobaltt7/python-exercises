# 145
digits = sorted(input("number:"))
print(digits[0], digits[-1])

# 146
from math import sqrt

number1 = int(input("number:"))
number2 = int(input("number:"))
print(number1 ** (1 / 3) == sqrt(number2))

# 147
numbers = input("numbers:").split()
first = sum(map(int, numbers.pop(0)))
answer = True

for number in numbers:
    if not (first == sum(map(int, number))):
        answer = False
        break

print(answer)

# 148
numbers = list(map(int, input("numbers:").split()))
last = numbers.pop(0)
count = 0

for number in numbers:
    if number > last:
        count += 1
    last = number

print(count)

# 149
number = int(input("number:"))
print([[number] * number] * number)


# 150
def cbrt(number):
    return number * (1 / 3)


number = cbrt(int(input("number:")))
count = 1

while number > 3:
    number = cbrt(number)
    count += 1

print(count)
