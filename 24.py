"""
Calculates millionth lexicographic permutation of 0-9 in numerical order.

Problem set from Project Euler
http://projecteuler.net
Problem 24

@author Russ Taylor <russ@russt.me>
@version 2014-08-25
"""

import itertools

combinations = tuple(itertools.permutations(range(10)))

print(combinations[999999])
