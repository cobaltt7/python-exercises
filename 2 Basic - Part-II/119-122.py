# 119
a = int(input("a:"))
b = int(input("b:"))


def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(a, b) == 1)

# 120
number = int(input("number:"))


def gcd2(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    return gcd2(b, a % b)


print(1 if number == 1 else len([y for y in range(1, number) if gcd2(number, y) == 1]))

# 121
print(
    input("string:")
    .replace("P", "9")
    .replace("T", "O")
    .replace("S", "1")
    .replace("H", "6")
    .replace("A", "8")
)

# 122
uppercase = map(chr, range(65, 91))
string = input("string:")
print(all(char in uppercase for char in string))
