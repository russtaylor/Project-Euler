"""
Calculates the number of letters used in writing all the numbers from 1-1000 in words.

Problem set from Project Euler
http://projecteuler.net
Problem 17

@author Russ Taylor <russ@russt.me>
@version 2013-05-21
"""

import math

def roundDown(num, divisor):
  return num - (num % divisor)

def countForNumber(num):
  numString = str(num)
  if len(numString) == 1:
    return numberLengths[num]
  elif len(numString) == 2:
    if num < 20 or (num % 10) == 0:
      return numberLengths[num]
    else:
      letterCount = numberLengths[roundDown(num, 10)]
      letterCount += countForNumber(int(numString[1]))
      return letterCount
  elif len(numString) == 3:
    letterCount = numberLengths[int(numString[0])]
    letterCount += numberLengths[100]
    if int(numString[1:]) > 0:
      letterCount += 3 # To account for the 'and'
      letterCount += countForNumber(int(numString[1:]))
    return letterCount
  elif len(numString) == 4:
    return numberLengths[1] + numberLengths[1000]
  else:
    return 0

numberLengths = {
  1: 3,
  2: 3,
  3: 5,
  4: 4,
  5: 4,
  6: 3,
  7: 5,
  8: 5,
  9: 4,
  10: 3,
  11: 6,
  12: 6,
  13: 8,
  14: 8,
  15: 7,
  16: 7,
  17: 9,
  18: 8,
  19: 8,
  20: 6,
  30: 6,
  40: 5,
  50: 5,
  60: 5,
  70: 7,
  80: 6,
  90: 6,
  100: 7,
  1000: 8
}

letterCount = 0
for i in range(1,1001):
  print str(i) + ": " + str(countForNumber(i))
  letterCount += countForNumber(i)

print letterCount
