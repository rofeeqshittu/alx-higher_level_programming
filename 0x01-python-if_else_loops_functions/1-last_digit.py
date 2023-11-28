#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number1 = -number
    lastdigit = number1 % 10
    lastdigit = str(lastdigit)
    lastdigit = "-" + lastdigit
    lastdigit = int(lastdigit)
else:
    lastdigit = number % 10

if lastdigit > 5:
    print("Last digit of {} is {} and is greater than \
5".format(number, lastdigit))
elif lastdigit == 0:
    print("Last digit of {} is {} and is 0".format(number, lastdigit))
else:
    print("Last digit of {} is {} and \
is less than 6 and not 0".format(number, lastdigit))
