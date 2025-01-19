# 72
string = input("string:")
print("".join(reversed(string)) == string)

# 73
array = input("array:").split(",")
print(len(set(array)))

# 74
prices = list(map(float, input("prices:").split(",")))
max = 0
for index, buy in enumerate(prices):
    for sell in prices[(index + 1) :]:
        gain = sell - buy
        if gain > max:
            max = gain
print(max)

# 75
array = input("array:").split(",")
item = input("item:")
print(len(list(filter(lambda found: found != item, array))))

# 76
array = input("array:").split(",")
value = input("value:")
print((array.index(value), len(array) - (list(reversed(array)).index(value)) - 1))

# 77
prices = list(map(float, input("prices:").split(",")))
max = 0
for index, buy in enumerate(prices):
    for sell in prices[(index + 1) :]:
        gain = sell - buy
        if gain > max:
            max = gain
print(max)

# 78
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [0, 6, 2, 8], [2, 3, 0, 2]]
for index, line in enumerate(matrix):
    to_print = reversed(line) if index % 2 else line
    for number in to_print:
        print(number)
