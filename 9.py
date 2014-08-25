"""
Finds the pythagorean triplet a^2 + b^2 = c^2 where a + b + c = 1000

Problem set from Project Euler
http://projecteuler.net
Problem 9

@author Russ Taylor <russ@russt.me>
@version 2013-04-30
"""

import itertools

def fitsPythagorean(array):
    array.sort()
    if (array[0]**2 + array[1]**2 == array[2]**2):
        return True

for combination in itertools.combinations_with_replacement(range(1,500), 3):
    combinationList = list(combination)
    if combinationList[0] + combinationList[1] + combinationList[2] == 1000:
        if fitsPythagorean(combinationList):
            print "Found combination!", combinationList
            print "Product:", combinationList[0] * combinationList[1] * combinationList[2]
