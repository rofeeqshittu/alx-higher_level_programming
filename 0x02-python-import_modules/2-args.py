#!/usr/bin/python3
import sys

arg_len = len(sys.argv) - 1
if arg_len == 0:
    print("0 arguments.")
elif arg_len == 1:
    print("1 argument:")
    print(f"1: {sys.argv[1]}")
else:
    print(f"{arg_len} arguments:")
    for i in range(1, arg_len + 1):
        print(f"{i}: {sys.argv[i]}")
