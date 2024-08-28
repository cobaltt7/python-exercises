# 20
from math import factorial
from re import search

number = int(input("number:"))
factored = str(factorial(number))
zeros = search(r"0*$", factored).group()
print(len(zeros))

# 21
NOTES = [10, 20, 50, 100, 200, 500]


def subtractNote(number):
    matches = [note for note in NOTES if note <= number]
    return number - matches[-1] if len(matches) > 0 else None


i = 0
value = int(input("number:"))

while value != None:
    lastValue = value
    value = subtractNote(lastValue)
    i += 1

print("Notes:", i - 1)
print("Remainder:", lastValue)


# 22
def getNumberAtIndex(index):
    if index < 5:
        return 1
    return (
        getNumberAtIndex(index - 1)
        + getNumberAtIndex(index - 2)
        + getNumberAtIndex(index - 3)
        + getNumberAtIndex(index - 4)
    )


print(getNumberAtIndex(int(input("number:"))))

# 23
from functools import reduce


def substractSum(number):
    return number - reduce(lambda a, b: a + int(b), str(number), 0)


number = int(input("number:"))

while number > 0:
    number = substractSum(number)

print(number)

# 24
from math import ceil

number = int(input("number:"))
factors = set()

for i in range(ceil(number / 2)):
    if number % (i + 1) == 0:
        factors.add(i + 1)

for factor in set(factors):
    factors.add(int(number / factor))

print(sorted(factors))

# 25
ALL_DIGITS = range(10)
digits = [9, 8, 3, 2, 2, 0, 9, 7, 6, 3]
print([digit for digit in ALL_DIGITS if digit not in digits])

# 26
from functools import reduce

numbers = [1, 4, 5]
differences = []

for idx, i in enumerate(numbers):
    for j in numbers[idx + 1 :]:
        differences.append(abs(i - j))

print(reduce(lambda a, b: a + b, differences, 0))


# 27
def ap(numbers):
    difference = numbers[1] - numbers[0]
    if numbers[1] + difference == numbers[2]:
        return difference


def gp(numbers):
    factor = numbers[1] / numbers[0]
    if numbers[1] * factor == numbers[2]:
        return factor


SEQUENCE = [1, 3, 9]
difference = ap(SEQUENCE)
factor = gp(SEQUENCE)

if difference == None:
    print("GP,", SEQUENCE[-1] * factor)
else:
    print("AP,", SEQUENCE[-1] + difference)

# 28
from functools import reduce

series = [1, 2, 3, 4, 5]

print("3rd term:", series[2])
print("3rd to last term:", series[-3])
print("Sum:", reduce(lambda a, b: a + b, series, 0))
print("Length:", len(series))

# 29
from math import ceil

number1 = int(input("number:"))
number2 = int(input("number:"))


def get_factors(number):
    factors = set()

    for i in range(ceil(number / 2)):
        if number % (i + 1) == 0:
            factors.add(i + 1)

    for factor in set(factors):
        factors.add(int(number / factor))

    return factors


factors1 = get_factors(number1)
factors2 = get_factors(number2)

print([factor for factor in factors1 if factor in factors2])
