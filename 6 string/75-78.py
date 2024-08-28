def seventy_five(string: str):
    """
    Write a Python program to find smallest window that contains all characters of a
    given string.
    """
    out = string
    characters = set(string)
    while all(map(lambda char: char in out[1:], characters)):
        out = out[1:]
    while all(map(lambda char: char in out[:-1], characters)):
        out = out[:-1]
    return out


print(seventy_five("asdaewsqgtwwsa"))
assert seventy_five("asdaewsqgtwwsa") == "daewsqgt"


def seventy_six(string: str, k: int):
    """
    Write a Python program to count the number of substrings from a given string of
    lowercase alphabets with exactly k distinct (given) characters.
    """
    count = 0
    for i in range(len(string) - 3):
        substring = string[i : i + k]
        if len(substring) == len(set(substring)):
            count += 1
    return count


print(seventy_six("wolffffffwolf", 4))
assert seventy_six("wolffffffwolf", 4) == 3
assert seventy_six("wolffffff", 4) == 1
assert seventy_six("wolffffffwol", 4) == 2
assert seventy_six("wofl", 4) == 1


def seventy_seven(string: str):
    """
    Write a Python program to count number of non-empty substrings of a given string.
    """
    length = len(string)
    return int(length * (length + 1) / 2)


print(seventy_seven("w3resource"))
assert seventy_seven("w3resource") == 55
