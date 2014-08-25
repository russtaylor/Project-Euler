"""
Calculates the sum of the digits of 2^1000

Problem set from Project Euler
http://projecteuler.net
Problem 16

@author Russ Taylor <russ@russt.me>
@version 2013-05-01
"""

import math

number = 2**1000
numString = str(number)

sum = 0
for digit in numString:
    sum += int(digit)

print sum
