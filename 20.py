"""
Calculates the sum of the digits of 100!

Problem set from Project Euler
http://projecteuler.net
Problem 20

@author Russ Taylor <russ@russt.me>
@version 2014-08-17
"""

def calculateFactorial(x):
  product = 1
  for i in range(x,0,-1):
    product = product * i
  return product

def digitSum(x):
  sum = 0
  for i in str(x):
    sum = sum + int(i)
  return sum

print digitSum(calculateFactorial(100))
