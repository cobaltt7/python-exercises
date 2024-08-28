from re import split


def one_hundred_eight(string: str):
    """
    Write a Python program that takes a string and returns # on both sides of each element, which
    are not vowels.
    """
    return "".join(
        character if character in "aeiou" else f"-{character}-" for character in string
    )


print(one_hundred_eight("Green"))
assert one_hundred_eight("Green") == "-G--r-ee-n-"
assert one_hundred_eight("White") == "-W--h-i-t-e"
assert one_hundred_eight("aeiou") == "aeiou"


def one_hundred_nine(string: str):
    """
    Write a Python program that counts the number of leap years within the range of years. Ranges
    of years should be accepted as strings.
    """
    first, last = map(int, string.split("-"))
    count = 0
    for year in range(first, last + 1):
        if year % 4:
            continue
        if year % 100 or not year % 400:
            count += 1
    return count


print(one_hundred_nine("1979-1981"))
assert one_hundred_nine("1981-1991") == 2
assert one_hundred_nine("2000-2020") == 6
assert one_hundred_nine("1900-1901") == 0


def one_hundred_ten(one: str):
    """
    Write a Python program to insert space before every capital letter appears in a given word.
    """
    return " ".join(split(r"(?<=.)(?=[A-Z])", one))


print(one_hundred_ten("RedGreen"))
assert one_hundred_ten("RedGreen") == "Red Green"
assert one_hundred_ten("PythonExercises") == "Python Exercises"
assert one_hundred_ten("Python") == "Python"
assert (
    one_hundred_ten("PythonExercisesPracticeSolution")
    == "Python Exercises Practice Solution"
)
