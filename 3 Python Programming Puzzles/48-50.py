def fortyEight(data):
    """
    Write a Python program to find the indices of two entries that show that the list is not in
    increasing order. If there are no violations (they are increasing), return an empty list.
    """
    indices = [
        entry[0]
        for entry in enumerate(data)
        if entry[0] > 0 and data[entry[0] - 1] > entry[1]
    ]
    if len(indices) == 0:
        return []
    return [indices[0] - 1, indices[0]]


def fortyNine(data):
    """
    Write a Python program to find the h-index, the largest positive number h such that h occurs in
    the sequence at least h times. If there is no such positive number return h = -1.
    """
    counts = {}
    for number in sorted(data, reverse=True):
        if number not in counts:
            counts[number] = 0
        counts[number] = counts[number] + 1

        if counts[number] >= number:
            return number
    return -1


def fifty(data):
    """
    Write a Python program to find even-length words from a given list of words and sort them by
    length.
    """
    return sorted(
        filter(lambda word: len(word) % 2 == 0, data), key=lambda word: len(word)
    )


print(fortyEight([1, 2, 3, 0, 4, 5, 6]))
assert fortyEight([1, 2, 3, 0, 4, 5, 6]) == [2, 3]
assert fortyEight([1, 2, 3, 4, 5, 6]) == []
assert fortyEight([1, 2, 3, 4, 6, 5, 7]) == [4, 5]
assert fortyEight([-3, -2, -3, 0, 2, 3, 4]) == [1, 2]

print(fortyNine([1, 2, 2, 3, 3, 4, 4, 4, 4]))
assert fortyNine([1, 2, 2, 3, 3, 4, 4, 4, 4]) == 4
assert fortyNine([1, 2, 2, 3, 4, 5, 6]) == 2
assert fortyNine([3, 1, 4, 17, 5, 17, 2, 1, 41, 32, 2, 5, 5, 5, 5]) == 5

print(fifty(["Red", "Black", "White", "Green", "Pink", "Orange"]))
assert fifty(["Red", "Black", "White", "Green", "Pink", "Orange"]) == ["Pink", "Orange"]
assert fifty(
    ["The", "worm", "ate", "a", "bird", "imagine", "that", "!", "Absurd", "!!"]
) == ["!!", "worm", "bird", "that", "Absurd"]
