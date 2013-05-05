# Calculates the largest Collatz sequence under 1,000,000

# Problem set from Project Euler
# http://projecteuler.net
# Problem 14

# @author Russ Taylor <russ@russt.me>
# @version 2013-05-05

largestSequenceNumber = 0
largestSequenceCount = 0
for i in range(500000, 1000000):
    count = 0
    calcNum = i
    while calcNum > 1:
        if calcNum % 2 == 0:
            calcNum = calcNum / 2
        else:
            calcNum = 3 * calcNum + 1
        count += 1

    if count > largestSequenceCount:
        largestSequenceCount = count
        largestSequenceNumber = i

print largestSequenceNumber
