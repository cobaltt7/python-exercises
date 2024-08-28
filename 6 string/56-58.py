def fifty_six(string):
    """Write a Python program to find the second most repeated word in a given string."""
    counts = {}
    words = string.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return sorted(counts.items(), key=lambda entry: entry[1], reverse=True)[1]


a = fifty_six(
    "Both of these issues are fixed by postponing the evaluation of annotations."
    " Instead of compiling code which executes expressions in annotations at their"
    " definition time, the compiler stores the annotation in a string form equivalent"
    " to the AST of the expression in question. If needed, annotations can be resolved"
    " at runtime using typing.get_type_hints(). In the common case where this is not"
    " required, the annotations are cheaper to store (since short strings are interned"
    " by the interpreter) and make startup time faster."
)
print(a)
assert fifty_six(
    "Both of these issues are fixed by postponing the evaluation of annotations."
    " Instead of compiling code which executes expressions in annotations at their"
    " definition time, the compiler stores the annotation in a string form equivalent"
    " to the AST of the expression in question. If needed, annotations can be resolved"
    " at runtime using typing.get_type_hints(). In the common case where this is not"
    " required, the annotations are cheaper to store (since short strings are interned"
    " by the interpreter) and make startup time faster."
) == ("of", 4)


def fifty_seven(string):
    """Write a Python program to remove spaces from a given string."""
    return "".join(string.split())


print(fifty_seven("w 3 res ou r ce"))
assert fifty_seven("w 3 res ou r ce") == "w3resource"
assert fifty_seven("a b c") == "abc"
