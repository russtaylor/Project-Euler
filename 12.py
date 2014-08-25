"""
Calculates the first triangular number with 500 or more factors.

Problem set from Project Euler
http://projecteuler.net
Problem 12

@author Russ Taylor <russ@russt.me>
@version 2013-05-03
"""

import math

def calcNumberOfDivisors(number):
    divisors = [1,number]
    for x in xrange(2, int(math.sqrt(number))):
        divisor, remainder = divmod(number, x)
        if remainder == 0:
            divisors.append(x)
            divisors.append(divisor)
    return len(divisors)

currentNumber = 0
currentSum = 0
numDivisors = 0

while 500 > numDivisors:
    currentNumber += 1
    currentSum += currentNumber
    if currentSum:
        numDivisors = calcNumberOfDivisors(currentSum)

print currentSum
