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
    print(f"Last digit of {number} is {lastdigit} and is less than 5")
elif lastdigit == 0:
    print(f"Last digit of {number} is {lastdigit} and is 0")
else:
    print(f"Last digit of {number} is {lastdigit} and \
is less than 6 and not 0")
