def fifty_eight(string):
    """Write a Python program to move spaces to the front of a given string."""
    length = len(string)
    stripped = string.replace(" ", "")
    return (" " * (length - len(stripped))) + stripped


print(fifty_eight("w3resource .  com  "))
assert fifty_eight("w3resource .  com  ") == "     w3resource.com"
assert fifty_eight("   w3resource.com  ") == "     w3resource.com"


def fifty_nine(string):
    """Write a Python program to find the maximum occuring character in a given string."""
    counts = {}
    for character in string:
        if character not in counts:
            counts[character] = 0
        counts[character] = counts[character] + 1
    return sorted(counts.items(), key=lambda entry: entry[1], reverse=True)[0][0]


print(fifty_nine("Welcome to w3resource"))
assert fifty_nine("Welcome to w3resource") == "e"
assert fifty_nine("Python: Get file creation and modification date/times") == "t"
assert fifty_nine("abcdefghijkb") == "b"


def sixty(string: str):
    """
    Write a Python program to capitalize first and last letters of each word of a given string.
    """
    return " ".join(
        map(
            lambda word: word[0].upper() + word[1:-1] + word[-1].upper(), string.split()
        )
    )


print(sixty("python exercises practice solution"))
assert (
    sixty("python exercises practice solution") == "PythoN ExerciseS PracticE SolutioN"
)
assert sixty("w3resource") == "W3resourcE"
