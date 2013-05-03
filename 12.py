# Calculates the first triangular number.

# Problem set from Project Euler
# http://projecteuler.net
# Problem 12

# @author Russ Taylor <russ@russt.me>
# @version 2013-05-03

import math

def calcNumberOfDivisors(number):
    numberOfDivisors = 0
    currentDivisor = 0
    while currentDivisor <= (number / 2):
        currentDivisor += 1
        if number % currentDivisor == 0:
            numberOfDivisors += 1
    return numberOfDivisors

currentNumber = 0
currentSum = 0
numDivisors = 0

while numDivisors < 500:
    currentNumber += 1
    currentSum += currentNumber
    if currentNumber > 100000:
        numDivisors = calcNumberOfDivisors(currentNumber)

print currentNumber