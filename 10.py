# Calculates the sum of all primes less than 2,000,000

# Problem set from Project Euler
# http://projecteuler.net
# Problem 10

# @author Russ Taylor <russ@russt.me>
# @version 2013-04-30

import math

primes = [2,3,5,7]
termcalc = 11

while termcalc <= 2000000:
    
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
	
print 'Sum:', sum(primes)