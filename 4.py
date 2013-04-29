# Gets the largest pallindrome product of two three-digit numbers

# Problem set from Project Euler
# http://projecteuler.net
# Problem 4

# @author Russ Taylor <russ@russt.me>
# @version 2013-04-28

import array
import itertools

numberArray = range(100,105)

for pair in itertools.combinations_with_replacement(numberArray, 2):
    print pair
    
