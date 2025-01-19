# 47
from os import cpu_count

print(cpu_count())

# 48
string = input("number:")
print(float(string))
print(int(string))

# 49
from os import listdir

print(listdir())

# 50
print("Hel", end="")
print("lo,", end=" ")
print("world!")

# 51
import cProfile

cProfile.run('print("hi ")')

# 52
from sys import stderr

print("spam", file=stderr)

# 53
from os import environ

print(environ)

# 54
from os import path

print(path.expanduser("~"))

# 55
import socket

print(socket.gethostbyname_ex(socket.gethostname())[-1])

# 56
from shutil import get_terminal_size

columns, rows = get_terminal_size()
print(f"{rows}x{columns}")

# 57
import time

tic = time.perf_counter()
time.sleep(5)
toc = time.perf_counter()
print(toc - tic)

# 58
sum = 0

for i in range(int(input("number:")) + 1):
    sum += i

print(sum)
