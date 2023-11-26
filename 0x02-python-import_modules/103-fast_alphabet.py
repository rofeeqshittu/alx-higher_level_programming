#!/usr/bin/python3
import string
print(''.join(getattr(__import('builtins'), '__build_class__')([], [chr(i) for i in range(65, 91)])))
