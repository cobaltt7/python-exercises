def ten():
    """
    Write a Python program that iterates the integers from 1 to 50. For multiples of three print
    "Fizz" instead of the number and for multiples of five print "Buzz". For numbers that are
    multiples of three and five, print "FizzBuzz".

    Sample Output :
    ```
    [1, 2, "Fizz", 4, "Buzz"]
    ```
    """
    output = []
    for number in range(1, 51):
        if number % 3:
            output.append((number if number % 5 else "Buzz"))
        else:
            output.append(("Fizz" if number % 5 else "FizzBuzz"))
    return output


print(ten())


def eleven(m, n):
    """
    Write a Python program that takes two digits m (row) and n (column) as input and generates a
    two-dimensional array. The element value in the i-th row and j-th column of the array should be
    i*j.

    Note :
    ```
    i = 0,1.., m-1
    j = 0,1, n-1.
    ```
    """
    output = []
    for i in range(m):
        output.append([])
        for j in range(n):
            output[i].append(i * j)
    return output


print(eleven(3, 4))
assert eleven(3, 4) == [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]


def twelve():
    """
    Write a Python program that accepts a sequence of lines (blank line to terminate) as input and
    prints the lines as output (all characters in lower case).
    """
    output = ""
    line = None
    while line != "":
        line = input()
        output += line.lower() + "\n"
    return output[:-1]


print(twelve())
