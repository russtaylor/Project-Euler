"""
Calculates the sum of all positive integers which can't be written as the sum of
two abundant numbers.

Problem set from Project Euler
http://projecteuler.net
Problem 23

@author Russ Taylor <russ@russt.me>
@version 2014-08-22
"""

import math

from enum import Enum
Abundance = Enum("Abundance", "deficient perfect abundant")

def calculateDivisors(integer):
  divisors = []
  for i in range(1, math.floor(integer / 2 + 1)):
    if integer % i == 0:
      divisors.append(i)
  return divisors

def calculateAbundance(integer):
  divisorSum = sum(calculateDivisors(integer))
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

print(getAbundantBelow(28123))
