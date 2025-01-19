# 30
number = input("number:")
sum = int(number) + int(number[::-1])
sumStr = str(sum)
if sumStr != sumStr[::-1]:
    sum += int(sumStr[::-1])
print(sum)


# 31
def defaultToZero(number):
    return 0 if number == None else int(number)


number1 = input("number:")
number2 = input("number:")
sum = str(int(number1) + int(number2))

reversed1 = number1[::-1]
reversed2 = number2[::-1]
reversed_sum = sum[::-1]

carries = 0
for index in range(max([len(reversed1), len(reversed2)])):
    if (
        defaultToZero(reversed1[index]) + defaultToZero(reversed2[index])
    ) != reversed_sum[index]:
        carries += 1

print(carries)

# 32
heights = [25, 35, 15, 16, 30, 45, 37, 39]
print(sorted(heights, reverse=True)[:3])

# 33
numbers = list(map(int, input("numbers:").split(" ")))
print(len(str(numbers[0] + numbers[1])))

# 34
number1 = float(input("number:"))
number2 = float(input("number:"))
number3 = float(input("number:"))
print("Yes" if number1**2 + number2**2 == number3**2 else "No")

# 35
a, b, c, d, e, f = map(float, input("numbers:").split())
g = a * e - b * d
x = (c * e - b * f) / g
y = (a * f - c * d) / g
print({"x": x, "y": y})

# 36
from math import ceil

debt = float(input("debt:"))
months = int(input("months:"))

for month in range(months):
    debt = ceil(debt * 1.05 / 1000) * 1000

print(debt)

# 37
from itertools import product

number = int(input("number:"))
count = 0

for a, b, c, d in product(range(10), range(10), range(10), range(10)):
    if a + b + c + d == number:
        count += 1

print(count)

# 38
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
