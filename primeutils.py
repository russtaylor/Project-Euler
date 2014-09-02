from math import sqrt, ceil
import numpy

class PrimeUtils:
  """
  A simple class containing some basic functionality for calculations around
  prime numbers.
  """

  primes = []

  def __init__(self, maxPrime = 1000):
    self.calcPrimesTo(maxPrime)

  def calcPrimesTo(self, n):
    """
    Sets the class variable 'primes' to the list of primes up to the specified
    'n', where 'n' is >= 6.
    """
    if self.primes and self.primes[-1] >= n:
      return
    sieve = numpy.ones(n / 3 + (n % 6 == 2), dtype=numpy.bool)
    for i in range(1, ceil(int(n ** 0.5) / 3)):
      if sieve[i]:
        k = 3 * i + 1 | 1
        sieve[k * k / 3 :: 2 * k] = False
        sieve[k * (k - 2 * (i & 1) + 4 ) / 3 :: 2 * k] = False
    self.primes = numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)].tolist()

  def calculateAbundance(self, integer):
    divisorSum = sum(self.calculateDivisors(integer)) - integer
    if divisorSum > integer:
      return 1
    elif divisorSum < integer:
      return -1
    return 0

  def calculateFactors(self, n):
    """
    Returns a list of the prime factors of 'n', paired with the multiplicity of
    each.
    """
    upperBound = ceil(sqrt(n))
    self.calcPrimesTo(upperBound)
    for prime in self.primes:
      if prime > upperBound:
        break
      if n % prime == 0:
        multiplicity = 1
        while n % (prime ** (multiplicity + 1)) == 0:
          multiplicity += 1
        yield prime, multiplicity

  def calculateDivisors(self, n):
    """
    Returns a list of the proper divisors of 'n'.
    """
    divisors = [1, n]
    factors = self.calculateFactors(n)
    for factor in factors:
      for multiple in range(1,factor[1] + 1):
        divisors.append(factor[0]**multiple)
    print(n, sorted(divisors))
    return sorted(list(set(divisors)))
