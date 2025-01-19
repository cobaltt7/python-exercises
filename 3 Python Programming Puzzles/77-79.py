def seventySeven(data):
    """
    Write a Python program to convert GPAs to letter grades according to the following table:
    | GPAs   | Grades |
    |--------|--------|
    | 4.0:   | A+     |
    | 3.7:   | A      |
    | 3.4:   | A-     |
    | 3.0:   | B+     |
    | 2.7:   | B      |
    | 2.4:   | B-     |
    | 2.0:   | C+     |
    | 1.7:   | C      |
    | 1.4:   | C-     |
    | below: | F      |
    """

    def parse_grade(grade):
        if grade < 1.4:
            return "F"
        if grade < 1.7:
            return "C-"
        if grade < 2:
            return "C"
        if grade < 2.4:
            return "C+"
        if grade < 2.7:
            return "B-"
        if grade < 3:
            return "B"
        if grade < 3.4:
            return "B+"
        if grade < 3.7:
            return "A-"
        return "A" if grade < 4 else "A+"

    return [parse_grade(grade) for grade in data]


print(seventySeven([4.0, 3.5, 3.8]))
assert seventySeven([4.0, 3.5, 3.8]) == ["A+", "A-", "A"]
assert seventySeven([5.0, 4.7, 3.4, 3.0, 2.7, 2.4, 2.0, 1.7, 1.4, 0.0]) == [
    "A+",
    "A+",
    "A-",
    "B+",
    "B",
    "B-",
    "C+",
    "C",
    "C-",
    "F",
]


def seventyEight(data):
    """
    Write a Python program to find the two closest distinct numbers in a given list of numbers.
    """
    closest = []
    diff = None
    for index2, second in enumerate(data):
        for first in data[:index2]:
            test = abs(second - first)
            if test and (not diff or test < diff):
                diff = test
                closest = [first, second]
    return sorted(closest)


print(seventyEight([12.02, 20.3, 15.0, 19.0, 11.0, 14.99, 17.0, 17.0, 14.4, 16.8]))
assert seventyEight([1.3, 5.24, 0.89, 21.0, 5.27, 1.3]) == [5.24, 5.27]
assert seventyEight([12.02, 20.3, 15.0, 19.0, 11.0, 14.99, 17.0, 17.0, 14.4, 16.8]) == [
    14.99,
    15.0,
]


def seventyNine(data):
    """
    Write a Python program to find the largest negative and smallest positive numbers (or 0 if
    none).
    """
    neg = [number for number in data if number < 0]
    pos = [number for number in data if number > 0]
    return [max(neg) if len(neg) else 0, min(pos) if len(pos) else 0]


print(seventyNine([-12, -6, 300, -40, 2, 2, 3, 57, -50, -22, 12, 40, 9, 11, 18]))
assert seventyNine([-12, -6, 300, -40, 2, 2, 3, 57, -50, -22, 12, 40, 9, 11, 18]) == [
    -6,
    2,
]
assert seventyNine([-1, -2, -3, -4]) == [-1, 0]
assert seventyNine([1, 2, 3, 4]) == [0, 1]
assert seventyNine([]) == [0, 0]
