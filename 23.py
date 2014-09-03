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

def abundantSums(limit, abundantList):
  abundantSumList = [False] * (limit + 1)
  for i in abundantList:
    for j in abundantList:
      if(i + j <= limit):
        abundantSumList[i + j] = True
      else:
        break
  return abundantSumList

primeutils = PrimeUtils(20162)
abundantList = getAbundantBelow(20162, primeutils)
abundantSumList = abundantSums(20162, abundantList)
sum = 0
for index, abundant in enumerate(abundantSumList):
  if not abundant:
    sum += index

print(sum)
