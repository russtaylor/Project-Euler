"""
Calculates the number of valid lattice paths to the bottom of a 20x20 grid.

Problem set from Project Euler
http://projecteuler.net
Problem 15

@author Russ Taylor <russ@russt.me>
@version 2013-05-05
"""

# import time
# import math
# from itertools import repeat

# # Love the recursive functions
# def advance(array, index = None):
#     if index == None:
#         index = -1
#     array[index] = (array[index] + 1) % 2
#     if array[index] == 0 and math.fabs(index) < len(array):
#         advance(array, index - 1)

# numArray = list(repeat(0,40))

# count = 0
# for i in range(1,2**len(numArray)):
#     advance(numArray)
#     if sum(numArray) == 20:
#         count += 1

# print count

sum = 0
for i in range(1,20):
    sum += 2*i
    print sum