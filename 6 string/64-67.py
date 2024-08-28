def sixty_four(string: str):
    """Write a Python program to find maximum length of consecutive 0’s in a given binary string."""
    maximum = 0
    count = 0
    for char in string:
        if char == "0":
            count += 1
            if count > maximum:
                maximum = count
        else:
            count = 0
    return maximum


print(sixty_four("111000010000110"))
assert sixty_four("111000010000110") == 4
assert sixty_four("111000111") == 3


def sixty_five(one: str, two: str):
    """
    Write a Python program to find all the common characters in lexicographical order from two given
    lower case strings.
    """
    result = sorted(set(one.lower()).intersection(two.lower()))
    return result if len(result) else None


print(sixty_five("w3resource", "python and swift"))
assert sixty_five("w3resource", "python and swift") == ["o", "s", "w"]
assert sixty_five("Python", "PHP") == ["h", "p"]
assert sixty_five("Java", "PHP") is None


def sixty_seven(string: str):
    """Write a Python program to remove all consecutive duplicates of a given string."""
    out = ""
    last = ""
    for char in string:
        if not char == last:
            out += char
        last = char
    return out


print(sixty_seven("xxxxxyyyyy"))
assert sixty_seven("xxxxxyyyyy") == "xy"
assert sixty_seven("aaaaebbbb") == "aeb"
