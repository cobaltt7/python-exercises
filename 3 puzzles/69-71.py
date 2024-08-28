def sixtyNine(data):
    """
    Write a Python program to create a new string by taking a string, and word by word rearranging
    its characters in ASCII order.
    """
    return " ".join(["".join(sorted(word)) for word in data.split()])


print(sixtyNine("Ascii character table"))
assert sixtyNine("Ascii character table") == "Aciis aaccehrrt abelt"
assert sixtyNine("maltos won") == "almost now"


def seventy(data):
    """
    Write a Python program to find the first negative balance from a given list of numbers that
    represent bank deposits and withdrawals.
    """

    def func(array):
        sum = 0
        for number in array:
            sum += number
            if sum < 0:
                return sum

    return [func(array) for array in data]


print(seventy([[12, -7, 3, -89, 14, 88, -78], [-1, 2, 7]]))
assert seventy([[12, -7, 3, -89, 14, 88, -78], [-1, 2, 7]]) == [-81, -1]
assert seventy([[1200, 100, -900], [100, 100, -2400]]) == [None, -2200]


def seventyOne(data, seperator):
    """
    Given a list of numbers and a number to inject, write a Python program to create a list
    containing that number in between each pair of adjacent numbers.
    """
    output = []
    for number in data:
        output.append(number)
        output.append(seperator)
    output.pop()
    return output


print(seventyOne([12, -7, 3, -89, 14, 88, -78, -1, 2, 7], 6))
assert seventyOne([12, -7, 3, -89, 14, 88, -78, -1, 2, 7], 6) == [
    12,
    6,
    -7,
    6,
    3,
    6,
    -89,
    6,
    14,
    6,
    88,
    6,
    -78,
    6,
    -1,
    6,
    2,
    6,
    7,
]
assert seventyOne([1, 2, 3, 4, 5, 6], 9) == [1, 9, 2, 9, 3, 9, 4, 9, 5, 9, 6]
