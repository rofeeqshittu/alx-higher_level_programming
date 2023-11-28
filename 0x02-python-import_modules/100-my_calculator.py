#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

arg_len = len(sys.argv) - 1
if arg_len != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

a = int(sys.argv[1])
operator = sys.argv[2]
b = int(sys.argv[3])


if operator == '+':
    print("{} {} {} = {}".format(a, operator, b, add(a, b)))
elif operator == '-':
    print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
elif operator == '*':
    print("{} {} {} = {}".format(a, operator, b, div(mul(a, b))))
elif operator == '/':
    print("{} {} {} = {}".format(a, operator, b, div(a, b)))
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
