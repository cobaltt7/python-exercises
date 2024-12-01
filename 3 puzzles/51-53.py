from math import prod


def fiftyOne(n):
    """Find the first n Fibonacci numbers"""
    numbers = []
    for i in range(n):
        if i < 2:
            numbers.append(i)
        else:
            numbers.append(numbers[i - 1] + numbers[i - 2])
    return numbers


def fiftyTwo(data):
    """
    Write a Python program to reverse the case of all strings. For those strings, which contain no
    letters, reverse the strings.
    """

    def func(word: str):
        letters = map(
            lambda letter: letter.upper() if letter.islower() else letter.lower(), word
        )
        cased = "".join(letters)
        return "".join(reversed(word)) if cased == word else cased

    return list(map(func, data))


def fiftyThree(data):
    """
    Write a Python program to find the product of the units digits in the numbers in a given list.
    """
    digits = map(lambda number: int(str(number)[-1]), data)
    return prod(digits)


print(fiftyOne(10))
assert fiftyOne(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
assert fiftyOne(15) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
assert fiftyOne(50) == [
    0,
    1,
    1,
    2,
    3,
    5,
    8,
    13,
    21,
    34,
    55,
    89,
    144,
    233,
    377,
    610,
    987,
    1597,
    2584,
    4181,
    6765,
    10946,
    17711,
    28657,
    46368,
    75025,
    121393,
    196418,
    317811,
    514229,
    832040,
    1346269,
    2178309,
    3524578,
    5702887,
    9227465,
    14930352,
    24157817,
    39088169,
    63245986,
    102334155,
    165580141,
    267914296,
    433494437,
    701408733,
    1134903170,
    1836311903,
    2971215073,
    4807526976,
    7778742049,
]

print(
    fiftyTwo(
        [
            "cat",
            "catatatatctsa",
            "abcdefhijklmnop",
            "124259239185125",
            "",
            "foo",
            "unique",
        ]
    )
)
assert fiftyTwo(
    ["cat", "catatatatctsa", "abcdefhijklmnop", "124259239185125", "", "foo", "unique"]
) == ["CAT", "CATATATATCTSA", "ABCDEFHIJKLMNOP", "521581932952421", "", "FOO", "UNIQUE"]
assert fiftyTwo(["Green", "Red", "Orange", "Yellow", "", "White"]) == [
    "gREEN",
    "rED",
    "oRANGE",
    "yELLOW",
    "",
    "wHITE",
]
assert fiftyTwo(["Hello", "!@#", "!@#$", "123#@!"]) == [
    "hELLO",
    "#@!",
    "$#@!",
    "!@#321",
]

print(fiftyThree([12, 23]))
assert fiftyThree([12, 23]) == 6
assert fiftyThree([12, 23, 43]) == 18
assert fiftyThree([113, 234]) == 12
assert fiftyThree([1002, 2005]) == 10
