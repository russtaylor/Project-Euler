"""
Calculates the number of times that the first day of any month fell on a Sunday
between 1 Jan 1901 and 31 Dec 2000.

Problem set from Project Euler
http://projecteuler.net
Problem 19

@author Russ Taylor <russ@russt.me>
@version 2014-08-20
"""

from datetime import *
from dateutil.relativedelta import relativedelta

startDate = date(1901, 1, 1)
endDate = date(2000, 12, 31)

sundayCount = 0

while startDate < endDate:
  if(startDate.weekday() == 6):
    sundayCount = sundayCount + 1
  startDate = startDate + relativedelta(months=+1)

print sundayCount
