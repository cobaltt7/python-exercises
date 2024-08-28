from math import floor


def thirtySeven(month, day):
    """
    Write a Python program that reads two integers representing a month and day and prints the
    season for that month and day.
    """
    months = [
        "january",
        "februray",
        "march",
        "april",
        "may",
        "june",
        "july",
        "august",
        "september",
        "october",
        "november",
        "december",
    ]
    seasons = ["Winter", "Spring", "Summer", "Autumn"]
    index = months.index(month.lower()) + (day > 20)
    return seasons[floor(index / 3) % 4]


print(thirtySeven("july", 31))
assert thirtySeven("july", 31) == "Summer"
assert thirtySeven("december", 20) == "Autumn"
assert thirtySeven("december", 21) == "Winter"
assert thirtySeven("december", 31) == "Winter"


def thirtyEight(month, day):
    """Write a Python program to display the astrological sign for a given date of birth."""
    month = month.lower()
    if (month == "january" and day > 19) or (month == "february" and day < 19):
        return "Aquarius"

    if month == "february" or (month == "march" and day < 21):
        return "Pisces"

    if month == "march" or (month == "april" and day < 20):
        return "Aries"

    if month == "april" or (month == "may" and day < 21):
        return "Taurus"

    if month == "may" or (month == "june" and day < 21):
        return "Gemini"

    if month == "june" or (month == "july" and day < 23):
        return "Cancer"

    if month == "july" or (month == "august" and day < 23):
        return "Leo"

    if month == "august" or (month == "september" and day < 23):
        return "Virgo"

    if month == "september" or (month == "october" and day < 23):
        return "Libra"

    if month == "october" or (month == "november" and day < 22):
        return "scorpio"

    if month == "november" or (month == "december" and day < 21):
        return "sagittarius"

    return "Capricorn"


print(thirtyEight("may", 15))
assert thirtyEight("may", 15) == "Taurus"


def thirtyNine(year):
    """
    Write a Python program to display the sign of the Chinese Zodiac for the given year in which
    you were born.
    """
    return [
        "Dragon",
        "Snake",
        "Horse",
        "Sheep",
        "Monkey",
        "Rooster",
        "Dog",
        "Pig",
        "Rat",
        "Ox",
        "Tiger",
        "Hare",
    ][(year - 2000) % 12]


print(thirtyNine(1784))
assert thirtyNine(1784) == "Dragon"
