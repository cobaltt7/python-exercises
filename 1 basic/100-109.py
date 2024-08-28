# 100
from socket import gethostname

print(gethostname())

# 101
from requests import get

print(get(input("url:")).text)

# 102
from os import system

print(system("ls"))

# 103
import subprocess

result = subprocess.run(["ls"], stdout=subprocess.PIPE)
print(result.stdout.decode("utf-8"))

# 104
import os

print(os.getegid(), os.geteuid(), os.getgid(), os.getgroups())

# 105
from os import environ

print(environ)

# 106
from os import path

print(path.split(input("path:")))

# 107
from os import stat

print(stat(input("file:")))

# 108
from os.path import abspath

print(abspath(input("path:")))

# 109
number = float(input("number:"))
print("positive" if number > 0 else ("negative" if number < 0 else "zero"))
