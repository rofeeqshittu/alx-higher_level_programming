#!/usr/bin/python3
for i in range(97, 123):
    alpha = chr(i)
    if alpha == "q" or alpha == "e":
        continue
    print("{}".format(alpha), end='')
