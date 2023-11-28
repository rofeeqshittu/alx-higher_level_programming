#!/usr/bin/python3
for num in reversed(range(65, 91)):
    if num % 2 == 1:
        num = chr(num)
        print("{}".format(num), end='')
    else:
        num1 = chr(num).lower()
        print("{}".format(num1), end='')
