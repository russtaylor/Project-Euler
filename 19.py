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
from dateutil.relativedelta import relativedelta

beginDate = datetime.date(1901, 1, 1)
endDate = datetime.date(2000, 12, 31)

timeDelta = datetime.timedelta(months=1)

sundayCount = 0

def daterange(startDate, endDate):
  for n in range(int ((endDate - startDate).days)):
    yield startDate + timedelta(n)

for date in daterange(beginDate, endDate):
  if(date.weekday == 6):
    sundayCount = sundayCount + 1

print sundayCount
