# Calculates the largest prime factor of 600,851,475,143

# Problem set from Project Euler
# http://projecteuler.net
# Problem 3

# @author Russ Taylor <russ@russ-taylor.com>
# @version 2011-06-12

import math

number = 600851475143
primes = [2,3,5,7]
factors = []
termcalc = 11

# math.ceil(math.sqrt(number))
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