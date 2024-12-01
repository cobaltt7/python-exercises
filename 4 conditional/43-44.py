def fourtyThree(number):
    """Write a Python program to create the multiplication table (from 1 to 10) of a number."""
    out = {}
    for i in range(1, 11):
        out[i] = number * i
    return out


print(fourtyThree(6))
assert fourtyThree(6) == {
    1: 6,
    2: 12,
    3: 18,
    4: 24,
    5: 30,
    6: 36,
    7: 42,
    8: 48,
    9: 54,
    10: 60,
}


def fourtyFour():
    """Write a Python program to construct the following pattern, using a nested loop number."""
    out = ""
    for i in range(10):
        for _ in range(i):
            out += str(i)
        out += "\n"
    return out.strip()


print(fourtyFour())
assert (
    fourtyFour()
    == """1
22
333
4444
55555
666666
7777777
88888888
999999999"""
)
