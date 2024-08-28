from math import floor


def ninetyThree(data):
    """Write a Python program to find the closest palindrome to a given string."""
    output = [*data]
    for index, letter in enumerate(output):
        output[index * -1 - 1] = letter
    return "".join(output)


print(ninetyThree("cat"))
assert ninetyThree("cat") == "cac"
assert ninetyThree("madan") == "madam"
assert ninetyThree("radivider") == "radividar"
assert ninetyThree("madan") == "madam"
assert ninetyThree("abc") == "aba"
assert ninetyThree("racecbr") == "racecar"


def ninetyFour(data):
    """
    Given a string consisting of whitespace and groups of matched parentheses, write a Python
    program to split it into groups of perfectly matched parentheses without any whitespace.
    """
    open = 0
    segments = []
    segment = ""

    for char in data:
        if char == "(":
            open += 1
        elif char == ")":
            open -= 1

        if not char == " ":
            segment += char

        if open == 0 and segment != "":
            segments.append(segment)
            segment = ""

    return segments


print(ninetyFour("( ()) ((()()())) (()) ()"))
assert ninetyFour("( ()) ((()()())) (()) ()") == ["(())", "((()()()))", "(())", "()"]
assert ninetyFour("() (( ( )() ( )) ) ( ())") == ["()", "((()()()))", "(())"]


def ninetyFive(data, i):
    """Write a Python program to find a palindrome of a given length containing a given string."""
    segment = floor(i / 2)
    front = data[:segment]
    middle = data[segment] * (i % 2)
    back = data[len(data) - segment :]
    return front + middle + back


print(ninetyFive("madam", 7))
assert ninetyFive("madam", 7) == "madadam"
assert ninetyFive("madam", 6) == "maddam"
assert ninetyFive("madam", 5) == "madam"
assert ninetyFive("madam", 3) == "mam"
assert ninetyFive("madam", 2) == "mm"
assert ninetyFive("madam", 1) == "m"


def ninetySix(data):
    """
    Write a Python program to get the single digits in numbers sorted backwards and converted into
    English words.
    """
    numbers = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    filtered = filter(lambda number: 0 < number < 10, data)
    return list(map(lambda number: numbers[number], sorted(filtered, reverse=True)))


print(ninetySix([1, 3, 4, 5, 11]))
assert ninetySix([1, 3, 4, 5, 11]) == ["five", "four", "three", "one"]
assert ninetySix([27, 3, 8, 5, 1, 31]) == ["eight", "five", "three", "one"]
