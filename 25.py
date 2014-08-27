"""
Calculates the first fibonacci number with 1,000 digits.

Problem set from Project Euler
http://projecteuler.net
Problem 25

@author Russ Taylor <russ@russt.me>
@version 2014-08-25
"""

first = 1
second = 1

count = 3

while True:
  term = first + second
  if len(str(term)) == 1000:
    print(count)
    break
  first = second
  second = term
  count += 1
