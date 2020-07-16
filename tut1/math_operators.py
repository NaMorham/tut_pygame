#! /usr/bin/env python

# Math operators

import math

num1 = 10
num2 = 3

print("{} * {} = {}".format(num1, num2, num1*num2))
print("{} ^ {} = {}".format(num1, num2, num1 ^ num2))

print("{} / {} = {}".format(num1, num2, num1/num2))
print("{} // {} = {}".format(num1, num2, num1//num2))
print("{} % {} = {}".format(num1, num2, num1%num2))

print("{} + {} = {}".format(num1, num2, num1 + num2))

print("{} - {} = {}".format(num1, num2, num1 - num2))

print("round({} / {}) = {}".format(num1, num2, round(num1 / num2)))

print("round({} / {}, 1) = {}".format(num1, num2, round(num1 / num2, 1)))

print("math.floor({} / {}) = {}".format(num1, num2, math.floor(num1 / num2)))

print("math.ceil({} / {}) = {}".format(num1, num2, math.ceil(num1 / num2)))

print("math.log10({}) = {}".format(num1, math.log10(num1)))

print("math.log10(99) = {}".format(num1, math.log10(99)))
print("math.log10(100) = {}".format(num1, math.log10(100)))
