# 102
from re import sub


def replace(string):
    result = sub(r"(.)\1", "\\1", string)
    return result if result == string else replace(result)


print(replace(input("string:")))

# 103
line1 = (2, 3, 4)
line2 = (2, 3, 8)
print(line1[0] / line1[1] == line2[0] / line2[1])

# 104
matrix = [[7, 5, 6], [3, 4, 4], [6, 5, 7]]


def get_column(index):
    return map(lambda row: row[index], matrix)


for row in matrix:
    index, minimum = min(enumerate(row), key=lambda item: item[1])
    if max(get_column(index)) == minimum:
        print(minimum)
        break


# 105
def is_linear(seq):
    diff = seq[1] - seq[0]
    return seq[1] + diff == seq[2]


def is_quadratic(seq):
    diff1 = seq[1] - seq[0]
    diff2 = seq[2] - seq[1]
    b_diff = diff2 - diff1
    diff3 = b_diff + diff2
    return seq[2] + diff3 == seq[3]


def is_cubic(seq):
    diff1 = seq[1] - seq[0]
    diff2 = seq[2] - seq[1]
    diff3 = seq[3] - seq[2]

    b_diff1 = diff2 - diff1
    b_diff2 = diff3 - diff2

    c_diff = b_diff2 - b_diff1

    b_diff3 = b_diff2 + c_diff
    diff4 = diff3 + b_diff3

    return seq[3] + diff4 == seq[4]


sequence = [1, 2, 3, 4, 5]
if is_linear(sequence):
    print("linear")
elif is_quadratic(sequence):
    print("quadratic")
elif is_cubic(sequence):
    print("cubic")
else:
    print("unknown")
