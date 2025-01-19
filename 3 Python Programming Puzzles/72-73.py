def seventyTwo(data):
    """
    Write a Python program to find the indices of three numbers that sum to 0 in a given list of
    numbers.
    """
    for i1, first in enumerate(data):
        for i2, second in enumerate(data[i1 + 1 :]):
            for i3, third in enumerate(data[i2 + i1 + 2 :]):
                if first + second + third == 0:
                    return [i1, i2 + i1 + 1, i3 + i2 + i1 + 2]


print(seventyTwo([1, 2, 3, 4, 5, 6, -7]))
assert seventyTwo([12, -7, 3, -89, 14, 4, -78, -1, 2, 7]) == [1, 2, 5]
assert seventyTwo([1, 2, 3, 4, 5, 6, -7]) == [0, 5, 6]


def seventyThree(data):
    """
    Write a Python program to find a substring in a given string that contains a vowel between two
    consonants.
    """
    string = ""
    for letter in data:
        if letter in "aeiouAEIOU":
            if len(string) == 1:
                string += letter
            else:
                string = ""
        else:
            if len(string) < 2:
                string = letter
            else:
                return string + letter


print(seventyThree("Python"))
assert seventyThree("Hello") == "Hel"
assert seventyThree("Sandwhich") == "San"
assert seventyThree("Python") == "hon"
