# Calculates 10,001st prime number.

# Problem set from Project Euler
# http://projecteuler.net
# Problem 7

# @author Russ Taylor <russ@russt.me>
# @version 2013-04-29

import math

primes = [2,3,5,7]
termcalc = 11

while len(primes) <= 10000:
    
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

    termcalc += 2
	
print '10,001st Prime:', primes[-1]