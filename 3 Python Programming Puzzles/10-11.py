# 9
def eNine(data):
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


assert eNine("( ()) ((()()())) (()) ()") == ["(())", "((()()()))", "(())", "()"]
assert eNine("() (( ( )() ( )) ) ( ())") == ["()", "((()()()))", "(())"]


# 11
def eEleven(data, threshold):
    return list(
        map(
            lambda entry: entry[0],
            filter(lambda entry: entry[1] < threshold, enumerate(data)),
        )
    )


assert eEleven([0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55], 100) == [
    0,
    1,
    2,
    3,
    7,
    8,
    9,
    10,
]
assert eEleven([0, 12, 4, 3, 49, 9, 1, 5, 3], 10) == [0, 2, 3, 5, 6, 7, 8]
