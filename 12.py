# Calculates the first triangular number with 500 or more factors.

# Problem set from Project Euler
# http://projecteuler.net
# Problem 12

# @author Russ Taylor <russ@russt.me>
# @version 2013-05-03

import math

def primesTo(limit, primeList):
    number = primeList[-1]
    while number < limit:
        isPrime = True

        for prime in primeList:
            if number % prime == 0:
                isPrime = False
                break

        if isPrime == True:
            primeList.append(number)

        number += 2
    return primeList

def calcNumberOfDivisors(number, primeList):
    primes = primesTo(number, primeList)
    divisors = [1,number]
    for prime in primeList:
        if number % prime == 0:
            divisors.append(prime)
            count = 2
            while (count * prime) < number:
                if number % (count * prime) == 0:
                    divisors.append(count * prime)
                count += 1
    return set(divisors), primeList

primes = [2,3,5,7]
currentNumber = 0
currentSum = 0
numDivisors = 0

while numDivisors <= 500:
    currentNumber += 1
    currentSum += currentNumber
    if currentSum > 10000000:
        divisors, primes = calcNumberOfDivisors(currentSum, primes)
        print numDivisors
        numDivisors = len(divisors)

print currentSum