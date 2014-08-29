from math import sqrt, ceil
import numpy

class PrimeUtils:
  """
  A simple class containing some basic functionality for calculations around
  prime numbers.
  """

  primes = []

  def calcPrimesTo(self, n):
      """
      Sets the class variable 'primes' to the list of primes up to the specified
      'n', where 'n' is >= 6.
      """
      sieve = numpy.ones(n / 3 + (n % 6 == 2), dtype=numpy.bool)
      for i in range(1, ceil(int(n ** 0.5) / 3)):
        if sieve[i]:
          k = 3 * i + 1 | 1
          sieve[k * k / 3 :: 2 * k] = False
          sieve[k * (k - 2 * (i & 1) + 4 ) / 3 :: 2 * k] = False
      self.primes = numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)].tolist()

  def calculateDivisors(self, n):
    """
    Returns a list of the proper divisors of 'n', excepting 'n' itself.
    """
    divisors = [1]
    upperBound = ceil(sqrt(n))
    self.calcPrimesTo(upperBound)
    for prime in self.primes:
      if prime > upperBound:
        break
      if n % prime == 0:
        divisors.append(prime)
        divisors.append(int(n / prime))
        for 
    return sorted(list(set(divisors)))
