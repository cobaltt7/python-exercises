def fifty_three(string):
    """Write a Python program to find the first repeated character in a given string."""
    for character in string:
        if character in string[string.index(character) + 1 :]:
            return character


print(fifty_three("abcdabcd"))
assert fifty_three("abcdabcd") == "a"
assert fifty_three("abcdbcd") == "b"
assert fifty_three("abcd") is None


def fifty_four(string):
    """
    Write a Python program to find the first repeated character of a given string where the index of
    first occurrence is smallest.
    """
    for index, character in enumerate(string):
        if character in string[string.index(character) + 1 :]:
            return (index, character)


print(fifty_four("ababc"))
assert fifty_four("ababc") == (0, "a")
assert fifty_four("abcb") == (1, "b")
assert fifty_four("abcc") == (2, "c")
assert fifty_four("abcxxy") == (3, "x")
assert fifty_four("abc") is None


def fifty_five(string):
    """Write a Python program to find the first repeated word in a given string."""
    words = string.split()
    for word in words:
        if word in words[words.index(word) + 1 :]:
            return word


print(fifty_five("ab ca bc ab"))
assert fifty_five("ab ca bc ab") == "ab"
assert fifty_five("ab ca bc") is None
