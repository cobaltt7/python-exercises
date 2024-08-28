def twenty_five(string, shift=13):
    """
    Write a Python program to create a Caesar encryption.

    Note: In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher,
    Caesar's code or Caesar shift, is one of the simplest and most widely known encryption
    techniques. It is a type of substitution cipher in which each letter in the plaintext is
    replaced by a letter some fixed number of positions down the alphabet. For example, with a left
    shift of 3, D would be replaced by A, E would become B, and so on. The method is named after
    Julius Caesar, who used it in his private correspondence.
    """
    return "".join(
        [chr(ord(char) + shift) if char.isalnum() else char for char in string]
    )


print(twenty_five("abC"))
assert twenty_five("abC") == "noP"
assert twenty_five("abc", 2) == "cde"


def twenty_six(string):
    """
    Write a Python program to display formatted text (width=50) as output.
    """
    string = string.strip().split()
    out = []
    line = ""
    for word in string:
        old_line = line
        line += word + " "
        if len(line) > 50:
            out.append(old_line.strip())
            line = word + " "
    out.append(line.strip())
    return "\n".join(out)


print(twenty_six("""
  Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.
  """))
assert (
    twenty_six("""
  Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.
  """)
    == """Python is a widely used high-level,
general-purpose, interpreted, dynamic programming
language. Its design philosophy emphasizes code
readability, and its syntax allows programmers to
express concepts in fewer lines of code than
possible in languages such as C++ or Java."""
)


def twenty_seven(string):
    """
    Write a Python program to remove existing indentation from all of the lines in a given text.
    """
    return "\n".join([string.strip() for string in string.split("\n")]).strip()


print(twenty_seven("""
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    """))
assert (
    twenty_seven("""
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    """)
    == """Python is a widely used high-level, general-purpose, interpreted,
dynamic programming language. Its design philosophy emphasizes
code readability, and its syntax allows programmers to express
concepts in fewer lines of code than possible in languages such
as C++ or Java."""
)


def twenty_eight(string, prefix="> "):
    """Write a Python program to add prefix text to all of the lines in a string."""
    return "\n".join([prefix + string.strip() for string in string.strip().split("\n")])


print(twenty_eight("""
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    """))
assert (
    twenty_eight("""
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    """)
    == """> Python is a widely used high-level, general-purpose, interpreted,
> dynamic programming language. Its design philosophy emphasizes
> code readability, and its syntax allows programmers to express
> concepts in fewer lines of code than possible in languages such
> as C++ or Java."""
)


def twenty_nine(string):
    """Write a Python program to set the indentation of the first line."""
    return "\n".join(
        ["    " + string.strip() for string in string.strip().split("\n")]
    ).strip()


print(twenty_nine("""
Python is a widely used high-level, general-purpose, interpreted, dynamic
programming language. Its design philosophy emphasizes code readability,
and its syntax allows programmers to express concepts in fewer lines of
code than possible in languages such as C++ or Java.
    """))
assert (
    twenty_nine("""
Python is a widely used high-level, general-purpose, interpreted, dynamic
programming language. Its design philosophy emphasizes code readability,
and its syntax allows programmers to express concepts in fewer lines of
code than possible in languages such as C++ or Java.
    """)
    == """Python is a widely used high-level, general-purpose, interpreted, dynamic
    programming language. Its design philosophy emphasizes code readability,
    and its syntax allows programmers to express concepts in fewer lines of
    code than possible in languages such as C++ or Java."""
)
