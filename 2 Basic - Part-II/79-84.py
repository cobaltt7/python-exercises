# 79
numbers = list(enumerate(map(float, input("numbers:").split())))

max_product = 0
for index1, number1 in numbers:
    for index2, number2 in numbers[(index1 + 1) :]:
        for index3, number3 in numbers[(index2 + 1) :]:
            product = number1 * number2 * number3
            if product > max_product:
                max_product = product

print(max_product)

# 80
numbers = list(map(int, input("numbers:").split()))

to_find = sorted(numbers, key=abs)[0]
while to_find in numbers:
    to_find += 1
print(to_find)

# 81
from random import sample

min = int(input("min:"))
max = int(input("max:"))
count = int(input("count:"))

print(sample(range(min + min % 2, max + 1, 2), k=count))

# 82
import math

numbers = list(map(float, input("numbers:").split()))
numbers.sort()

length = len(numbers)
middle = length / 2

if length % 2 == 0:
    print((numbers[int(middle) - 1] + numbers[int(middle)]) / 2)
else:
    print(numbers[math.floor(middle)])

# 83
string = input("string:")
print("".join(reversed(string)) == string)

# 84
numbers = list(map(float, input("numbers:").split()))

negatives = 0
sum = 0

for number in numbers:
    if number > 0:
        sum += number
    else:
        negatives += 1

print([negatives, sum])
