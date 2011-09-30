# Calculates the sum of the even fibonacci numbers
# up to 4,000,000

# Problem set from Project Euler
# http://projecteuler.net
# Problem 2

# @author Russ Taylor <russ@russ-taylor.com>
# @version 2011-06-09

sum = 0
term0 = 0
term1 = 1
term2 = 1

while term2 < 4000000:
	
	if term2 % 2 == 0:
		sum += term2
		
	term0 = term1
	term1 = term2
	
	term2 = term0 + term1
	
print 'sum:', sum