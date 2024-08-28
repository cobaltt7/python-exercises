# 130
print("double")
print("single")

# 131
string = input("string:")
print(string[:10])
print(string[10:])

# 132
from os import path

home = path.expanduser("~")
print(path.relpath(home) + "/")

# 133
from datetime import datetime
from time import sleep

start = datetime.now()
sleep(0.5)
print(datetime.now() - start)

# 134
numbers = input("numbers:").split(" ")
print(list(map(float, numbers)))

# 135
x = 30
print(f'Value of x is "{x}"')

# 136
from glob import glob

print(glob("./[!venv]**", recursive=True))

# 137
dict = {"a": "abc", "b": "def"}
b = dict["b"]
print(b)

# 138
print(int(True))
print(int(False))

# 139
ip = input("ip:")
numbers = ip.split(".")
print(
    len(numbers) == 4
    and all((number.isnumeric() and 255 >= int(number) >= 0) for number in numbers)
)
