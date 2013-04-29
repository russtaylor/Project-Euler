# Gets the largest palindrome product of two three-digit numbers

# Problem set from Project Euler
# http://projecteuler.net
# Problem 4

# @author Russ Taylor <russ@russt.me>
# @version 2013-04-28

import array
import itertools

def integer_is_palindrome(integer):
    return string_is_palindrome(str(integer))

def string_is_palindrome(string):
    if len(string) < 2:
        return True
    if string[0] != string[-1]:
        return False
    return string_is_palindrome(string[1:-1])

palindrome = 0

numberArray = range(100,1000)

for pair in itertools.combinations_with_replacement(numberArray, 2):
    product = pair[0] * pair[1]
    if integer_is_palindrome(product) and product > palindrome:
        palindrome = product

print palindrome
