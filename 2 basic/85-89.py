# 85
string = input("string:")
length = len(string)
char_count = len(set(string))
print(length % char_count == 0)

# 86
numbers = input("numbers:").split()
reversed_numbers = list(reversed(numbers))
last_index = len(numbers) - 1
count = 0

for index, number in enumerate(numbers):
    if (
        numbers.index(number) != index
        or (last_index - reversed_numbers.index(number)) != index
    ):
        count += 1

print(count)

# 87
code = input("code:")
length = len(code)
print(code.isdigit() and (length == 8 or length == 12))

# 88
string = input("string:")
characters = input("characters:")

present = True
for character in characters:
    if character not in string:
        present = False
        break

print(present)

# 89
numbers = sorted(map(float, input("numbers:").split()))
sum = 0
count = 0

for number in numbers:
    if number < 0:
        continue
    sum += number
    count += 1
    if count == 3:
        break

print(sum)
