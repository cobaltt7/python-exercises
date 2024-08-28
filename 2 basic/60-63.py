# 60
from re import findall

words = findall(r"\w+", input("string:"))
print(sorted(set(filter(lambda word: len(word) > 2, words))))

# 61
from sys import stdin

sum = 0
last_index = 0
last_count = 1
for line in stdin:
    numbers = line.split()
    count = len(numbers)
    alternative_index = last_index + (
        1 if count > last_count else (0 if last_index == 0 else -1)
    )
    number1 = float(numbers[alternative_index if last_index == count else last_index])
    number2 = float(numbers[alternative_index])
    if number2 > number1:
        sum += number2
        last_index = alternative_index
    else:
        sum += number1
    last_count = count

print(sum)

# 62
print(int(input("number:")) * 10000)

# 63
from functools import reduce

size = int(input("number:"))

rows = []
for index in range(size):
    row = list(map(float, input("row:").split()))
    row_sum = reduce(lambda acc, item: acc + item, row, 0)
    row.append(row_sum)
    rows.append(row)

rows.append([])
for columnIndex in range(size + 1):
    column_sum = 0
    for rowIndex in range(size):
        number = rows[rowIndex][columnIndex]
        column_sum += number
    rows[-1].append(column_sum)

print("\n".join(["\t".join([str(item) for item in row]) for row in rows]))
