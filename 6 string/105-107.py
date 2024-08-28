from re import sub


def one_hundred_five(string: str):
    """
    Write a Python program to extract and display the name from a given Email address.
    """
    return "".join(
        character
        for character in string.split("@")[0].split("+")[0]
        if character.isalpha()
    )


print(one_hundred_five("john@example.com"))
assert one_hundred_five("john@example.com") == "john"
assert one_hundred_five("john.smith@example.com") == "johnsmith"
assert one_hundred_five("fully-qualified-domain@example.com") == "fullyqualifieddomain"
assert (
    one_hundred_five("disposable.style.email.with+symbol@example.com@example.com")
    == "disposablestyleemailwith"
)


def one_hundred_six(string: str):
    """
    Write a Python program to remove repeated consecutive characters and replace them
    with single letters and print a updated string.
    """
    return sub(r"(.)\1+", lambda match: match.group(1), string)


print(one_hundred_six("Red Green White"))
assert one_hundred_six("Red Green White") == "Red Gren White"
assert one_hundred_six("aabbbcdeffff") == "abcdef"
assert one_hundred_six("Yellowwooddoor") == "Yelowodor"


def one_hundred_seven(one: str, two: str):
    """
    Write a Python program that takes two strings. Count the number of times each
    string contains the same three letters at the same index.
    """
    count = 0
    length = len(two)
    for index in range(len(one) - 2):
        if index < length and one[index : index + 3] == two[index : index + 3]:
            count += 1
    return count


print(one_hundred_seven("Red", "RedGreen"))
assert one_hundred_seven("Red", "RedGreen") == 1
assert one_hundred_seven("Red White", "Red White") == 7
assert one_hundred_seven("Red White", "White Red") == 0
