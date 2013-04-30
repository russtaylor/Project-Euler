# Gets the smallest number evenly divisible by all numbers from 1-20

# Problem set from Project Euler
# http://projecteuler.net
# Problem 5

# @author Russ Taylor <russ@russt.me>
# @version 2013-04-29

currentNumber = 2520
foundNumber = False

while foundNumber == False:
    currentNumber += 2520
    for divisor in range(1,21):
        if currentNumber % divisor != 0:
            break
        if divisor == 20:
            foundNumber = True

print currentNumber