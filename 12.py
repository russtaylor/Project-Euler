# Calculates the first triangular number with 500 or more factors.

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
    if currentSum > 10000000:
        numDivisors = calcNumberOfDivisors(currentSum)
        print numDivisors

while termcalc < (math.ceil(math.sqrt(number))):
    isPrime = True
    
    termcalcSqrt = math.sqrt(termcalc)
    
    for prime in primes:
        if prime > termcalcSqrt:
            break
        if termcalc % prime == 0:
            isPrime = False
            break
        
    if isPrime == True:
        primes.append(termcalc)
        if number % termcalc == 0:
            factors.append(termcalc)

    termcalc += 2
    
print 'factors:', factors

print currentSum