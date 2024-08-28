# 1
def eOne(array):
    nineteen = 0
    five = 0

    for number in array:
        if number == 19:
            nineteen += 1
        if number == 5:
            five += 1

    return nineteen == 2 and five > 2


assert eOne([19, 19, 15, 5, 3, 5, 5, 2]) == True
assert eOne([19, 15, 15, 5, 3, 3, 5, 2]) == False
assert eOne([19, 19, 5, 5, 5, 5, 5]) == True


# 2
def eTwo(array):
    fifths = 0

    for number in array:
        if number == array[4]:
            fifths += 1

    return len(array) == 8 and fifths == 3


assert eTwo([19, 19, 15, 5, 5, 5, 1, 2]) == True
assert eTwo([19, 15, 5, 7, 5, 5, 2]) == False
assert eTwo([11, 12, 14, 13, 14, 13, 15, 14]) == True
assert eTwo([19, 15, 11, 7, 5, 6, 2]) == False


# 3
def eThree(number):
    return number > 4**4 and number % 34 == 4


assert eThree(922) == True
assert eThree(914) == False
assert eThree(854) == True
