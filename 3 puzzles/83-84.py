def eightyThree(data):
    """
    A string is happy if every three consecutive characters are distinct. Write a Python program to
    find two indices associated with a given string being unhappy.
    """
    prevPrev = None
    prev = None
    for index, char in enumerate(data):
        if prevPrev == char:
            return [index - 2, index]
        if prev == char:
            return [index - 1, index]
        prevPrev = prev
        prev = char


print(eightyThree("Unhappy"))
assert eightyThree("Python") is None
assert eightyThree("Unhappy") == [4, 5]
assert eightyThree("Find") is None
assert eightyThree("Street") == [3, 4]


def eightyFour(data):
    """
    Write a Python program to find the index of the matching parentheses for each character in a
    given string.
    """
    output = [-1] * len(data)
    stack = []
    for index, char in enumerate(data):
        if char == "(":
            stack.append(index)
        else:
            output[stack[-1]] = index
            output[index] = stack.pop()
    return output


print(eightyFour("()(())"))
assert eightyFour("()(())") == [1, 0, 5, 4, 3, 2]
assert eightyFour("()()()") == [1, 0, 3, 2, 5, 4]
assert eightyFour("((()))") == [5, 4, 3, 2, 1, 0]
