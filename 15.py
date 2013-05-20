"""
Calculates the number of valid lattice paths to the bottom of a 20x20 grid.

Problem set from Project Euler
http://projecteuler.net
Problem 15

@author Russ Taylor <russ@russt.me>
@version 2013-05-19
"""

max = 20
gridSize = max + 1
grid = [[0] * gridSize] * gridSize
for i in range(max + 1):
    print "i:", i
    for j in range (i):
        if j == 0:
            grid[i][j] = 1
        elif len(grid[i-1]) < j:
            grid[i][j] = grid[i][j-1] * 2
        else:
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
print grid