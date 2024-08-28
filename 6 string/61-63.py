def sixty_one(string: str):
    """Write a Python program to remove duplicate characters of a given string."""
    return "".join(dict.fromkeys(string))


print(sixty_one("python exercises practice solution"))
assert sixty_one("python exercises practice solution") == "python exrcisalu"
assert sixty_one("w3resource") == "w3resouc"


def sixty_two(string: str):
    """Write a Python program to compute sum of digits of a given string."""
    acc = 0
    for character in string:
        if character.isnumeric():
            acc += int(character)
    return acc


print(sixty_two("123abcd45"))
assert sixty_two("123abcd45") == 15
assert sixty_two("abcd1234") == 10


def sixty_three(string: str):
    """Write a Python program to remove leading zeros from an IP address."""
    return ".".join([str(int(segment)) for segment in string.split(".")])


print(sixty_three("255.024.01.01"))
assert sixty_three("255.024.01.01") == "255.24.1.1"
assert sixty_three("127.0.0.01") == "127.0.0.1"
