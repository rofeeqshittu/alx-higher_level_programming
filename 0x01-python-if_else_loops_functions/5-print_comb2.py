#!/usr/bin/python3
for num in range(99):
    if num < 10:
        num1 = str(num)
        num = '0' + num1
    print("{}".format(num), end=', ')
num += 1
print("{}".format(num))
