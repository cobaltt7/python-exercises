def thirteen(numbers):
    """
    Write a Python program that accepts a sequence of comma separated 4 digit binary numbers as its
    input. The program will print the numbers that are divisible by 5 in a comma separated sequence.
    """
    decimals = map(lambda number: int(number, base=2), numbers.split(","))
    filtered = filter(lambda number: number % 5 == 0, decimals)
    return ",".join(map(lambda number: bin(number)[2:], filtered))


print(thirteen("0100,0011,1010,1001,1100,1001"))
assert thirteen("0100,0011,1010,1001,1100,1001") == "1010"


def fourteen(data):
    """
    Write a Python program that accepts a string and calculates the number of digits and letters.
    """
    output = [0, 0]
    for char in data:
        if char.isalpha():
            output[0] += 1
        elif char.isnumeric():
            output[1] += 1
    return output


print(fourteen("Python 3.2"))
assert fourteen("Python 3.2") == [6, 2]


def fifteen(password):
    """
    Write a Python program to check the validity of passwords input by users.

    Validation :
    - At least 1 letter between [a-z] and 1 letter between [A-Z].
    - At least 1 number between [0-9].
    - At least 1 character from [$#@].
    - Minimum length 6 characters.
    - Maximum length 16 characters.
    """
    length = len(password)
    if length < 6 or length > 16:
        return False

    hasalpha = False
    hasAlpha = False
    hasnum = False
    hassym = False
    for char in password:
        if char.islower():
            hasalpha = True
        if char.isupper():
            hasAlpha = True
        if char.isnumeric():
            hasnum = True
        if char in "$#@":
            hassym = True
    return hasalpha and hasAlpha and hasnum and hassym


print(fifteen("......aA0$......."))
assert fifteen("") is False
assert fifteen("A0$...") is False
assert fifteen("a0$...") is False
assert fifteen("aA$...") is False
assert fifteen("aA0...") is False
assert fifteen("aA0$") is False
assert fifteen("......aA0$......") is True
assert fifteen("......aA0$.......") is False
