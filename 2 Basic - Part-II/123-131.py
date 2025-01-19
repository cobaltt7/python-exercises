# 123
print(input("string:")[1:-1])

# 124
from re import search

print(bool(search(r"(.)\1", input("string:"))))

# 125
print("".join(reversed(input("string:"))).lower())

# 126
print("".join(sorted(input("string:"))))

# 127
from functools import reduce

numbers = input("numbers:").split()
sum = reduce(lambda acc, number: acc + float(number), numbers, 0)
print(sum % len(numbers) == 0)

# 128
from re import sub

print(sub(r"[aeiouAEIOU]", "", input("string:")))

# 129
string = input("string:")
entries = enumerate(string)
filtered = filter(lambda entry: entry[1].islower(), entries)
indicies = map(lambda entry: entry[0], filtered)
print(list(indicies))

# 130
from datetime import date

day = date(int(input("year:")), int(input("month:")), 13).strftime("%A")
print(day == "Monday")

# 131
from collections import Counter

counts = Counter(bin(int(input("number:"))))
print((counts.get("0") - 1, counts.get("1")))
