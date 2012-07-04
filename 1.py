# Calculates the sum of all natural numbers below
# 1000 that are divisible by 3 or 5

# Problem set from Project Euler
# http://projecteuler.net
# Problem 1

# @author Russ Taylor <russ@russ-taylor.com>
# @version 2011-06-09

sum = 0

for i in range (1, 1000):
	if (i % 3 == 0) or (i % 5 == 0) :
		sum += i

print 'sum', sum