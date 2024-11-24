def eight_five(x: int, y: int):
    """Write a Python program to create a multidimensional list (lists of lists) with zeros."""
    return [[0 for _ in range(x)] for _ in range(y)]


print(eight_five(2, 3))
assert eight_five(2, 3) == [[0, 0], [0, 0], [0, 0]]


def eight_six(x: int, y: int):
    """Write a Python program to create a 3X3 grid with numbers."""
    return [list(range(1, x + 1)) for _ in range(y)]


print(eight_six(3, 3))
assert eight_six(3, 3) == [[1, 2, 3], [1, 2, 3], [1, 2, 3]]


def eight_seven(data: str):
    """
    Write a Python program to read a matrix from the console and print the sum for each column. As
    input from the user, accept matrix rows, columns, and elements separated by a space (each row).
    """
    matrix = [[float(item) for item in row.split(" ")] for row in data.split("\n")]
    return tuple(
        sum(row[col_ind] for row in matrix) for col_ind in range(len(matrix[0]))
    )


print(eight_seven("1 2\n3 4"))
assert eight_seven("1 2\n3 4") == (4, 6)
