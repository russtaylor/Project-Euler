"""
Calculates the sum of all positive integers which can't be written as the sum of
two abundant numbers.

Problem set from Project Euler
http://projecteuler.net
Problem 23

@author Russ Taylor <russ@russt.me>
@version 2014-08-22
"""

from math import sqrt, ceil
import numpy

from enum import Enum
Abundance = Enum("Abundance", "deficient perfect abundant")

class PrimeUtils:
  """
  A simple class containing some basic functionality for calculations around
  prime numbers.
  """

  primes = []

  def calcPrimesTo(self, n):
      """ Input n>=6, Returns a array of primes, 2 <= p < n """
      sieve = numpy.ones(n / 3 + (n % 6 == 2), dtype=numpy.bool)
      for i in range(1, ceil(int(n ** 0.5) / 3)):
        if sieve[i]:
          k = 3 * i + 1 | 1
          sieve[k * k / 3 :: 2 * k] = False
          sieve[k * (k - 2 * (i & 1) + 4 ) / 3 :: 2 * k] = False
      self.primes = numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)].tolist()

  def calculateDivisors(self, integer):
    divisors = []
    upperBound = ceil(sqrt(integer))
    self.calcPrimesTo(upperBound)
    for i in self.primes:
      if integer % i == 0:
        divisors.append(i)
        divisors.append(int(integer / i))
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

def isSumOfAbundant(integer, abundantList):
  for i in abundantList:
    return

primeutils = PrimeUtils()
print(primeutils.calculateDivisors(16))

# print(getAbundantBelow(28123))
