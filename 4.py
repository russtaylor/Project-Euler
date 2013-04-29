# Gets the largest palindrome product of two three-digit numbers

# Problem set from Project Euler
# http://projecteuler.net
# Problem 4

# @author Russ Taylor <russ@russt.me>
# @version 2013-04-28

import array
import itertools

numberArray = range(100,1000)

for pair in itertools.combinations_with_replacement(numberArray, 2):
    print pair
    

def is_palindrome(integer):
    string = str(integer)