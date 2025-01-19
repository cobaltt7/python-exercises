# 11
x = [10, 20, 20, 20]
y = [10, 20, 30, 40]
z = [10, 30, 40, 20]
target = 70

for x_item in x:
    for y_item in y:
        for z_item in z:
            sum = x_item + y_item + z_item
            if sum == target:
                print((x_item, y_item, z_item))

# 12
numbers = [1, 2, 3]

length = len(numbers)
for i in numbers:
    for j in numbers:
        if i == j:
            continue
        for k in numbers:
            if i == k or j == k:
                continue
            print((i, j, k))

# 13
one = "def"
two = "ghi"

for char1 in one:
    for char2 in two:
        print(char1 + char2)

# 14
one = int(input("number:"))
two = int(input("number:"))

while two > 0:
    carry = one & two
    one = one ^ two
    two = carry << 1

print(one)

# 15
priorities = {"+": 0, "-": 0, "*": 1, "/": 1}


def test_higher_priority(operator1, operator2):
    return priorities[operator1] >= priorities[operator2]


print(test_higher_priority("*", "-"))
print(test_higher_priority("+", "-"))
print(test_higher_priority("+", "*"))
print(test_higher_priority("+", "/"))
print(test_higher_priority("*", "/"))

# 16
from math import sqrt

opposite = int(input("opposite:"))
adjacent = int(input("adjacent:"))

print(sqrt(opposite**2 + adjacent**2))


# 17
def gen_strobogrammatic(n, length=None):
    if length is None:
        length = n
    if n == 0:
        return [""]
    if n == 1:
        return ["1", "0", "8"]
    middles = gen_strobogrammatic(n - 2, length)
    result = []
    for middle in middles:
        if n != length:
            result.append("0" + middle + "0")
        result.append("8" + middle + "8")
        result.append("1" + middle + "1")
        result.append("9" + middle + "6")
        result.append("6" + middle + "9")
    return result


print(gen_strobogrammatic(2))
print(gen_strobogrammatic(3))
print(gen_strobogrammatic(4))

# 18
import math

numbers = [25, 15, 35]
numbers.sort()

length = len(numbers)
middle = length / 2

if length % 2 == 0:
    print(numbers[math.floor(middle)] + numbers[math.ceil(middle)])
else:
    print(numbers[int(middle)])

# 19
numbers = input("numbers:")
i = 0
count = 0
while i < len(numbers):
    count += 1
    next_char = numbers[i]
    i += 1
    while not int(next_char) == 2**count:
        next_char += numbers[i]
        i += 1

print(count)
