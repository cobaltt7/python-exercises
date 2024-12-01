def seven(datalist):
    """
    Write a Python program that prints each item and its corresponding type from the following
    list.
    """
    return list(map(lambda item: (item, type(item)), datalist))


print(
    seven(
        [
            1452,
            11.23,
            1 + 2j,
            True,
            "w3resource",
            (0, -1),
            [5, 12],
            {"class": "V", "section": "A"},
        ]
    )
)


def eight():
    """
    Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

    Note : Use `continue` statement.
    """
    output = []
    for number in range(6):
        if number == 3:
            continue
        output.append(number)
    return output


print(eight())
assert eight() == [0, 1, 2, 4, 5]


def nine():
    """
    Write a Python program to get the Fibonacci series between 0 and 50.

    Note : The Fibonacci Sequence is the series of numbers :
    ```
    0, 1, 1, 2, 3, 5, 8, 13, 21, ....
    ```
    Every next number is found by adding up the two numbers before it.
    """
    prev = 0
    next = 1
    output = []
    while next < 50 and len(output) < 50:
        output.append(next)
        next = next + prev
        prev = output[-1]
    return output


print(nine())
assert nine() == [1, 1, 2, 3, 5, 8, 13, 21, 34]
