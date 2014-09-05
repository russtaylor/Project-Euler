"""
Calculates the longest repeated pattern in a decimal from a unit fraction from
2-1000

Problem set from Project Euler
http://projecteuler.net
Problem 26

@author Russ Taylor <russ@russt.me>
@version 2014-09-04
"""

repeatedLength = 0
number = 0

for i in range(1000, 2, -1):
  if repeatedLength >= i:
    break

  remainders = [0] * i
  value = 1
  position = 0

  while remainders[value] == 0 and value != 0:
    remainders[value] = position
    value *= 10
    value %= i
    position += 1

  if position - remainders[value] > repeatedLength:
    number = i
    repeatedLength = position - remainders[value]

print(number)
