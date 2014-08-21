"""
Calculates the number of times that the first day of any month fell on a Sunday
between 1 Jan 1901 and 31 Dec 2000.

Problem set from Project Euler
http://projecteuler.net
Problem 19

@author Russ Taylor <russ@russt.me>
@version 2014-08-20
"""

import datetime

sundayCount = 0

for i in range(1901, 2001):
  for j in range(1, 13):
    if(datetime.date(i, j, 1).weekday() == 6):
      sundayCount += 1

print sundayCount
