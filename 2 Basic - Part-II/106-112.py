# 106
number = input("number:")

float(number)

missing = list(filter(lambda digit: str(digit) not in str(number), range(10)))
print(len(missing) == 0)

# 107
number = input("number:")
sum = 0

for digit in number:
    sum += int(digit)

print("Oddish" if sum % 2 else "Evenish")

# 108
number1 = int(input("number:")[-1])
number2 = int(input("number:")[-1])
expected = int(input("number:")[-1])

sum = number1 + number2
ending = int(str(sum)[-1])
print(ending == expected)

# 109
numbers = [1, 2, 3, 4, 5, 2]
number = 7

entries = enumerate(numbers)
filtered = filter(lambda found: found[1] == number, entries)
indicies = map(lambda entries: entries[0], filtered)

print(list(indicies))


# 110
def rindex(list, item):
    return len(list) - 1 - list[::-1].index(item)


numbers = list(map(float, input("numbers:").split()))
filtered = []

for number in numbers:
    if numbers.index(number) == rindex(numbers, number):
        filtered.append(number)

print(filtered)

# 111
from math import sqrt

# a, b = circle
# 1 = x
# 2 = y
# 3 = radius
a1, a2, a3, b1, b2, b3 = map(float, input("circles:").split())

x = (b1 - a1) ** 2
y = (b2 - a2) ** 2
r = a3 + b3
d = sqrt(x + y)

print(d <= r)

# 112
number1 = input("number:")
number2 = input("number:")

sum = 0
for index, digit1 in enumerate(number1):
    digit2 = int(number2[index])
    sum += abs(int(digit1) - int(digit2))

print(sum)
