#!/usr/bin/python3
import sys

arg_len = len(sys.argv) - 1
if arg_len == 0:
    print("{} arguments.".format(0))
elif arg_len == 1:
    print("{} argument:".format(0))
    print("{}: {}".format(1, sys.argv[1]))
else:
    print("{} arguments:".format(arg_len))
    for i in range(1, arg_len + 1):
        print("{}: {}".format(i, sys.argv[i]))
