"""
Calculates the sum of all positive integers which can't be written as the sum of
two abundant numbers.

Problem set from Project Euler
http://projecteuler.net
Problem 23

@author Russ Taylor <russ@russt.me>
@version 2014-08-22
"""

from enum import Enum
from primeutils import PrimeUtils

Abundance = Enum("Abundance", "deficient perfect abundant")

def calculateAbundance(self, integer):
  divisorSum = sum(self.calculateDivisors(integer))
  if divisorSum > integer:
    return Abundance.abundant
  elif divisorSum < integer:
    return Abundance.deficient
  return Abundance.perfect

def getAbundantBelow(integer):
  abundantNumbers = []
  for i in range(1, integer + 1):
    if calculateAbundance(i) == Abundance.abundant:
      abundantNumbers.append(i)
  return abundantNumbers

def isSumOfAbundant(integer, abundantList):
  for i in abundantList:
    return

primeutils = PrimeUtils()
print(primeutils.calculateDivisors(24))

# print(getAbundantBelow(28123))
