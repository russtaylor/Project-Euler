"""
Calculates the sum of all positive integers which can't be written as the sum of
two abundant numbers.

Problem set from Project Euler
http://projecteuler.net
Problem 23

@author Russ Taylor <russ@russt.me>
@version 2014-08-22
"""

from primeutils import PrimeUtils

def getAbundantBelow(integer, primeutils):
  abundantNumbers = []
  for i in range(1, integer + 1):
    if primeutils.calculateAbundance(i) == 1:
      abundantNumbers.append(i)
  return abundantNumbers

def isSumOfAbundant(integer, abundantList):
  for i in abundantList:
    return

primeutils = PrimeUtils()

print(getAbundantBelow(28123, primeutils))
