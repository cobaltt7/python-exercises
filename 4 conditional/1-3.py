from random import randint


def one():
    """
    Write a Python program to find those numbers which are divisible by 7 and multiples of 5,
    between 1500 and 2700 (both included).
    """
    return [number for number in range(1500, 2701) if not number % 7 and not number % 5]


print(one())


def two(data, mode="F"):
    """
    Write a Python program to convert temperatures to and from Celsius and Fahrenheit.

    [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
    """
    return data / (5 / 9) + 32 if mode == "C" else (data - 32) * 5 / 9


print(two(15, "F"))
assert two(60, "C") == 140
assert two(15, "F") == -9.444444444444445


def three():
    """
    Write a Python program to guess a number between 1 and 9.

    Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears
    again until the guess is correct, on successful guess, user will get a "Well guessed!" message,
    and the program will exit.
    """
    number = str(randint(1, 9))
    while input("number:") != number:
        continue
    print("Well guessed!")


three()
