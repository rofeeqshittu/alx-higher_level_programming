#!/usr/bin/python3
import sys

length = len(sys.argv) - 1
if length == 0:
    print(0)
elif length == 1:
    print(sys.argv[1])
else:
    sum = 0
    for i in range(1, length + 1):
        sum = sum + int(sys.argv[i])
    print(sum)
