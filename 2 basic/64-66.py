# 64
numbers = list(map(float, input("numbers:").split()))
number = float(input("number:"))


def function():
    for index, number1 in enumerate(numbers):
        for number2 in numbers[(index + 1) :]:
            if number1 + number2 == number:
                print(True)
                return


function()

# 65
word = "Green"
subseqs = {"Gn", "Gren", "ree", "en"}


def check_subseq(subseq):
    for letter in subseq:
        if letter not in word:
            return False

    return True


longest = None
for subseq in subseqs:
    if check_subseq(subseq) and (len(subseq) > len(longest) if longest else True):
        longest = subseq

print(longest)

# 66
from functools import reduce

seen = set()


def sum_squares(number):
    return reduce(lambda acc, digit: acc + int(digit) ** 2, str(number), 0)


def is_happy(number):
    if number == 1:
        return True

    if number in seen:
        return False

    seen.add(number)
    return is_happy(sum_squares(number))


print(is_happy(int(input("number:"))))
