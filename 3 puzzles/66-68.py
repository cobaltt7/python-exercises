def sixtySix(data):
    """
    Write a Python program to find the indices of the closest pair from a list of numbers.
    """
    closest = []
    diff = None
    for index2, second in enumerate(data):
        for index1, first in enumerate(data[:index2]):
            test = abs(second - first)
            if diff is None or test < diff:
                diff = test
                closest = [index1, index2]
    return closest


print(sixtySix([1, 7, 9, 2, 10]))
assert sixtySix([1, 7, 9, 2, 10]) == [0, 3]
assert sixtySix([1.1, 4.25, 0.79, 1.0, 4.23]) == [1, 4]
assert sixtySix([0.21, 11.3, 2.01, 8.0, 10.0, 3.0, 15.2]) == [2, 5]


def sixtySeven(data, shift):
    """
    Write a Python program to find a string which, when each character is shifted (ASCII
    incremented) by shift, gives the result.
    """
    return "".join([chr(ord(character) - shift) for character in data])


print(sixtySeven("Ascii character table", 1))
assert sixtySeven("Ascii character table", 1) == "@rbhhbg`q`bsdqs`akd"
assert sixtySeven("Ascii character table", -1) == "Btdjj!dibsbdufs!ubcmf"


def sixtyEight(n):
    """
    Write a Python program to find all 5's in integers less than n that are divisible by 9 or 15.
    """
    return [
        [number, str(number).index("5")]
        for number in range(n)
        if (number % 9 == 0 or number % 15 == 0) and "5" in str(number)
    ]


print(sixtyEight(50))
assert sixtyEight(50) == [[15, 1], [45, 1]]
assert sixtyEight(65) == [[15, 1], [45, 1], [54, 0]]
assert sixtyEight(75) == [[15, 1], [45, 1], [54, 0]]
assert sixtyEight(85) == [[15, 1], [45, 1], [54, 0], [75, 1]]
assert sixtyEight(150) == [[15, 1], [45, 1], [54, 0], [75, 1], [105, 2], [135, 2]]
