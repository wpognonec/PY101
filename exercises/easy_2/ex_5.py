# pylint: disable-all
import operator as op

'''
Write a program that prompts the user for two positive numbers (floating-point),
then prints the results of the following operations on those two numbers: addition,
subtraction, product, quotient, floor quotient, remainder, and power. Do not worry about validating the input.
'''

ops = {
    "+": op.add,
    "-": op.sub,
    "*": op.mul,
    "/": op.truediv,
    "//": op.floordiv,
    "%": op.mod,
    "**": op.pow,
}

num1 = float(input("==> Please enter first number: "))
num2 = float(input("==> Please enter second number: "))

for symbol in ops:
    print(f"==> {num1} {symbol} {num2} = {ops[symbol](num1, num2)}")
