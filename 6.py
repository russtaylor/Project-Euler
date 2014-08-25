"""
Finds the difference in the sum of the squares of the first 100 natural numbers and the square of
the sum of the first 100 natural numbers.

Problem set from Project Euler
http://projecteuler.net
Problem 6

@author Russ Taylor <russ@russt.me>
@version 2013-04-29
"""

sumSquares = 0
squareSums = 0

for i in range(1,101):
    sumSquares += i**2
    squareSums += i

squareSums = squareSums**2

print sumSquares
print squareSums

print "Difference: ", squareSums - sumSquares
