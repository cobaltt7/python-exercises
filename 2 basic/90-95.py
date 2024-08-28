# 90
string = input("string:")
print(("*" * (len(string) - 5)) + string[-5:])

# 91
data = None

if type(data) == tuple:
    print(len(data))
elif data == None:
    print(0)
else:
    print(1)

# 92
numbers = list(map(float, input("numbers:").split()))
if len(numbers) == 0:
    print([])
else:
    mapped = [numbers[0]]
    for number in numbers[1:]:
        mapped.append(mapped[-1] + number)
    print(mapped)

# 93
from math import floor

string = input("string:")
middle = len(string) / 2
if middle.is_integer():
    print(string[int(middle - 1)] + string[int(middle)])
else:
    print(string[floor(middle)])

# 94
numbers = list(map(float, input("numbers:").split()))
max_product = 0

for index, number in list(enumerate(numbers))[1:]:
    product = numbers[index - 1] * number
    if product > max_product:
        max_product = product

print(max_product)

# 95
numbers = list(map(float, input("numbers:").split()))

matches = True
for index, number in enumerate(numbers):
    if (index % 2) != (number % 2):
        matches = False
        break

print(matches)
