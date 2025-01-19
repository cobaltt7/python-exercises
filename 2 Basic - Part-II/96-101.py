# 96
number = input("number:")
digits = len(number)
sum = 0
for digit in number:
    sum += int(digit) ** digits
print(sum == number)

# 97
numbers = map(float, input("numbers:").split())

max = 0
min = 0
for number in numbers:
    if number > max:
        max = number
    if number < min:
        min = number

print((max, min))

# 98
numbers = list(map(float, input("numbers:").split()))

increasing = True
last = numbers[0]
for number in numbers[1:]:
    if not number > last:
        increasing = False
        break

print(increasing)

# 99
string = input("string:")
substring = input("substring:")
try:
    print(string.index(substring, string.index(substring) + 1))
except ValueError:
    print(-1)

# 100
numbers = list(map(float, input("numbers:").split()))
sum = 0

for index, number in enumerate(numbers):
    sum += index * number

print(sum)

# 101
input = {
    "Bernita Ahner": 12,
    "Kristie Marsico": 11,
    "Sara Pardee": 14,
    "Fallon Fabiano": 11,
    "Nidia Dominique": 15,
}

oldest = None
for name in input:
    if not oldest or input[name] > input[oldest]:
        oldest = name

print(oldest)
