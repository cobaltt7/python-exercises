# 39
from math import sqrt

x1, y1, x2, y2, x3, y3 = map(float, input("numbers:").split())

midpointAB = ((x1 + x2) / 2, (y1 + y2) / 2)
midpointBC = ((x2 + x3) / 2, (y2 + y3) / 2)

bisectorAB = -1 / ((y2 - y1) / (x2 - x1))
bisectorBC = -1 / ((y3 - y2) / (x3 - x2))

x = (
    (bisectorAB * midpointAB[0])
    - (bisectorBC * midpointBC[0])
    + midpointBC[1]
    - midpointAB[1]
) / (bisectorAB - bisectorBC)
y = bisectorAB * (x - midpointAB[0]) + midpointAB[1]

radius = sqrt(((x - x1) ** 2) + ((y - y1) ** 2))

print(radius)
print((x, y))


# 40
def calculate_area(a, b, c):
    return abs((a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2)


a1, a2, b1, b2, c1, c2, p1, p2 = map(float, input("numbers:").split())

areaABC = calculate_area((a1, a2), (b1, b2), (c1, c2))
areaPAB = calculate_area((p1, p2), (a1, a2), (b1, b2))
areaPAC = calculate_area((p1, p2), (a1, a2), (c1, c2))
areaPBC = calculate_area((p1, p2), (b1, b2), (c1, c2))

print(areaABC == (areaPAB + areaPAC + areaPBC))

# 41
number1 = int(input("number:"))
number2 = int(input("number:"))
sum = number1 + number2

if len(str(sum)) > 80:
    print("overflow")
else:
    print(sum)

# 42
numbers = list(map(float, input("numbers:").split()))
numbers.sort(reverse=True)
print(numbers)

# 43
p1, p2, q1, q2, r1, r2, s1, s2 = map(float, input("numbers:").split())

slopePQ = (q2 - p2) / (q1 - p1)
slopeRS = (s2 - r2) / (s1 - r1)

print(slopePQ == slopeRS)

# 44
count = int(input("count:"))

i = 0
sum = 0
while i < count:
    sum += float(input("number:"))
    i += 1

print(sum)
