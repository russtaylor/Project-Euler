"""
Calculates the sum of all amicable numbers less than 10,000

Problem set from Project Euler
http://projecteuler.net
Problem 21

@author Russ Taylor <russ@russt.me>
@version 2014-08-21
"""

def findDivisors(number):
  divisors = []
  for i in range(1, number / 2 + 1):
    if number % i == 0:
      divisors.append(i)
  return divisors

def isAmicable(number):
  numberSum = sum(findDivisors(number))
  if sum(findDivisors(numberSum)) == number and numberSum != number:
    return True
  return False

amicableNumbers = []

for i in range(1, 10000):
  if(isAmicable(i)):
    amicableNumbers.append(i)

print sum(amicableNumbers)
