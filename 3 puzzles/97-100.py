def ninetySeven(data):
    """
    Write a Python program to find the following strange sort of list of numbers: the first element
    is the smallest, the second is the largest of the remaining, the third is the smallest of the
    remaining, the fourth is the smallest of the remaining, etc.
    """
    output = []
    while len(data):
        output.append(max(data) if len(output) % 2 else min(data))
        data.remove(output[-1])
    return output


print(ninetySeven([1, 3, 4, 5, 11]))
assert ninetySeven([1, 3, 4, 5, 11]) == [1, 11, 3, 5, 4]
assert ninetySeven([27, 3, 8, 5, 1, 31]) == [1, 31, 3, 27, 5, 8]
assert ninetySeven([1, 2, 7, 3, 4, 5, 6]) == [1, 7, 2, 6, 3, 5, 4]


def ninetyEight(data):
    """
    Given a string consisting of groups of matched nested parentheses separated by parentheses,
    write a Python program to compute the depth of each group.
    """
    open = 0
    depth = 0
    output = []
    for bracket in data:
        if bracket == "(":
            open += 1
        elif bracket == ")":
            open -= 1
        depth = max(open, depth)
        if open == 0 and depth:
            output.append(depth)
            depth = 0
    return output


print(ninetyEight("(()) (()) () ((()()()))"))
assert ninetyEight("(()) (()) () ((()()()))") == [2, 2, 1, 3]
assert ninetyEight("() (()) () () () ()") == [1, 2, 1, 1, 1, 1]
assert ninetyEight("(((((((()))))))) () (()) ((()()()))") == [8, 1, 2, 3]


def ninetyNine(data):
    """
    Write a Python program to find a string such that, when three or more spaces are compacted to a
    '-' and one or two spaces are replaced by underscores, leads to the target.
    """
    return data.replace("-", "   ").replace("_", " ")


print(ninetyNine("Python-Exercises"))
assert ninetyNine("Python-Exercises") == "Python   Exercises"
assert ninetyNine("Python_Exercises") == "Python Exercises"
assert (
    ninetyNine("-Hello,_world!__This_is-so-easy!-")
    == "   Hello, world!  This is   so   easy!   "
)


def oneHundred(data):
    """Write a Python program to find four positive even integers whose sum is a given integer."""
    return [data - 6, 2, 2, 2]


print(oneHundred(100))
assert oneHundred(100) == [94, 2, 2, 2]
assert oneHundred(1000) == [994, 2, 2, 2]
assert oneHundred(10000) == [9994, 2, 2, 2]
assert oneHundred(1234567890) == [1234567884, 2, 2, 2]
