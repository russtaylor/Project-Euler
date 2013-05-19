"""
Calculates the number of valid lattice paths to the bottom of a 20x20 grid.

Problem set from Project Euler
http://projecteuler.net
Problem 15

@author Russ Taylor <russ@russt.me>
@version 2013-05-05
"""

grid = [[1]]
max = 20
for i in range(1,max):
    
    print sum