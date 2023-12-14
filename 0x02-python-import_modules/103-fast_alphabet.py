#!/usr/bin/python3
import string, functools
print(functools.reduce(lambda x, y: x + chr(y), map(ord, string.ascii_uppercase), ''))
