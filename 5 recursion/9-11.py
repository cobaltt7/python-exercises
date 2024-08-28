def nine(index):
    """
    Write a Python program to calculate the geometric sum of n-1.

    Note: In mathematics, a geometric series is a series with a constant ratio between successive
    terms.

    Example:
        ∞∑n=1 1/n = 1 + 1/2 + 1/3 + 1/4 + 1/5 + ....
    """
    return 0 if index < 0 else (1 / (2**index)) + nine(index - 1)


print(nine(3))
assert nine(7) == 1.9921875
assert nine(4) == 1.9375


def ten(a, b):
    """Write a Python program to calculate the value of 'a' to the power of 'b'."""
    return a**b


print(ten(3, 4))
assert ten(3, 4) == 81


def eleven(a, b):
    """Write a Python program to find the greatest common divisor (GCD) of two integers."""
    return a if b == 0 else eleven(b, a % b)


print(eleven(0, 14))
assert eleven(12, 14) == 2
