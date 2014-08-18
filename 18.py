"""
Calculates the largest sum of any route through adjacent numbers in a triangle
specified as follows:

    3
   7 4
  2 4 6
 8 5 9 3

Problem set from Project Euler
http://projecteuler.net
Problem 18

@author Russ Taylor <russ@russt.me>
@version 2014-08-18
"""

triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

def triToArray(triangleString):
  lines = triangleString.split('\n')
  grid = []
  for line in lines:
    grid.append([int(s) for s in line.split()])
  return grid

def calcRouteSum(triangleGrid):
  # Copy the list so we aren't modifying the original
  triangleCopy = list(triangleGrid)
  for i in range(len(triangleCopy) - 2,-1,-1):
    for j, value in enumerate(triangleCopy[i]):
      triangleCopy[i][j] = max(triangleCopy[i + 1][j] + value, triangleCopy[i + 1][j + 1] + value)
  return triangleCopy

# The solution will be whatever ends up in [0][0]
print calcRouteSum(triToArray(triangle))[0][0]
