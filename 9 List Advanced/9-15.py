from collections import OrderedDict
from typing import Any, Hashable


def nine(data: list[float]):
    """
    Write a Python a function to find the maximum sum sub-sequence in a list. Return
    the maximum value.
    """
    max_sum = 0.0
    current = 0.0
    for item in data:
        if item >= 0:
            current += item
        else:
            max_sum = max(max_sum, current)
            current = 0
    return max(max_sum, current)


print(nine([1, 2, 3]))
assert nine([1, 2, 3]) == 6
assert nine([1, 2, 4, 3, 5, 4, 6, 9, 2, -10]) == 36
assert nine([1, 2, -4, 3, 5, 4, 6, 9, 2, -10]) == 29
assert nine([1, 2, 4, 3, 5, -24, 6, 9, -2]) == 15


def ten(data: list[float]):
    """
    Write a Python a function to find the minimum sum sub-sequence in a list. Return
    the sub-sequence.
    """
    min_sum = 0.0
    min_start = 0
    min_end = 0
    current_sum = 0.0
    current_start = 0
    for index, item in enumerate(data):
        current_sum += item
        if current_sum > 0:
            current_sum = 0
            current_start = index + 1
        elif current_sum < min_sum:
            min_sum = current_sum
            min_start = current_start
            min_end = index
    return [min(data)] if min_sum == 0 else data[min_start : min_end + 1]


print(ten([1, 2, 6, 12]))
assert ten([1, 2, 6, 12]) == [1]
assert ten([1, -2, 4, 3, 5, 4, 6, 9, 2, -10]) == [-10]
assert ten([2, 4, -3, -5, -4, 6, 9, 2]) == [-3, -5, -4]
assert ten([1, 2, 4, 3, 5, -24, 4, 9, -22]) == [-24, 4, 9, -22]


def eleven(one: list[Any], two: list[Any]):
    """Write a Python function to find the longest common sub-sequence in two lists."""
    output: list[Any] = []
    for item in one:
        if two.count(item) > output.count(item):
            output.append(item)
    return output


print(eleven([3, 5, 1, 8, 8], [3, 3, 5, 3, 8]))
assert eleven([1, 2, 3, 4, 5, 6, 7, 8], [6, 7, 5, 6, 7, 8]) == [5, 6, 7, 8]
assert eleven([3, 5, 1, 8, 8], [3, 3, 5, 3, 8]) == [3, 5, 8]
assert not eleven([1, 3, 5, 7], [2, 4, 6, 8])
assert eleven([1, 3, 5, 7], [1, 2, 4, 6, 8]) == [1]


def twelve(data: list[Any]):
    """Write a Python program to find the first non-repeated element in a list."""
    for item in data:
        if data.count(item) == 1:
            return item
    return None


print(twelve([1, 2, 3, 4, 5, 6, 7, 8]))
assert twelve([1, 2, 3, 4, 5, 6, 7, 8]) == 1
assert twelve([1, 2, 3, 1, 2, 4, 5, 6, 7, 8]) == 3
assert twelve([1, 1, 2, 3, 1, 2, 3, 8, 8]) is None


class thirteen:
    """
    From Wikipedia -

    Least recently used (LRU)

    Discards the least recently used items first. This algorithm requires keeping track
    of what was used when, which is expensive if one wants to make sure the algorithm
    always discards the least recently used item. General implementations of this
    technique require keeping "age bits" for cache-lines and track the "Least Recently
    Used" cache-line based on age-bits. In such an implementation, every time a
    cache-line is used, the age of all other cache-lines changes. LRU is actually a
    family of caching algorithms with members including 2Q by Theodore Johnson and
    Dennis Shasha, and LRU/K by Pat O'Neil, Betty O'Neil and Gerhard Weikum.

    Write a Python a function to implement a LRU cache.
    """

    def __init__(self, max_size: int):
        self.max_size = max_size
        self.data = OrderedDict[Hashable, int]()

    def get(self, key: Hashable):
        if key in self.data:
            self.data.move_to_end(key)
            return self.data[key]
        return -1

    def put(self, key: Hashable, value: int):
        if len(self.data) == self.max_size:
            self.data.popitem(False)
        self.data[key] = value


cache = thirteen(2)
print(cache.data)
cache.put(10, 10)
print(cache.data)
cache.put(20, 20)
print(cache.data)
assert cache.get(10) == 10
print(cache.data)
cache.put(30, 30)
print(cache.data)
assert cache.get(20) == -1
print(cache.data)
cache.put(40, 40)
print(cache.data)
assert cache.get(10) == -1
print(cache.data)
assert cache.get(30) == 30
print(cache.data)
assert cache.get(40) == 40
print(cache.data)


def fourteen(lists: list[list[float]]):
    """Merge k Sorted Lists into a list"""
    return sorted(item for sublist in lists for item in sublist)


print(fourteen([[1, 2], [-1, -2, -3], [0]]))
assert fourteen([[1, 4, 5], [1, 3, 4], [2, 6, 7, 8]]) == [1, 1, 2, 3, 4, 4, 5, 6, 7, 8]
assert fourteen([[1, 2], [-1, -2, -3], [0]]) == [-3, -2, -1, 0, 1, 2]


def fifteen(data: list[float], target: float):
    """
    Write a Python program to find all the pairs in a list whose sum is equal to a
    given value.
    """
    output = set()
    for index, one in enumerate(data):
        for two in data[index + 1 :]:
            if one + two == target:
                output.add(frozenset({one, two}))
    return output


print(fifteen([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))
assert fifteen([1, 2, 3, 4, 5, 6, 7, 8, 9], 10) == {
    frozenset({6, 4}),
    frozenset({7, 3}),
    frozenset({8, 2}),
    frozenset({9, 1}),
}
assert not fifteen([1, 2, 3, 4, 5, 6, 7, 8, 9], 35)
assert fifteen([1, 2, 3, 4, 5, 6, 7, 8, 9], 5) == {frozenset({3, 2}), frozenset({4, 1})}
