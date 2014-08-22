"""
Calculates the 'value' of all names in the given text file

Problem set from Project Euler
http://projecteuler.net
Problem 23

@author Russ Taylor <russ@russt.me>
@version 2014-08-21
"""

inputPath = 'p022_names.txt'

def letterValue(letter):
  return ord(letter.lower()) - 96

def nameValue(name):
  value = 0
  for letter in name:
    value += letterValue(letter)
  return value

def loadFile():
  file = open(inputPath, 'r')
  untrimmedNames = file.read().split(',')
  names = []
  for name in untrimmedNames:
    names.append(name.replace('\"',''))
  return names

allNames = sorted(loadFile())
sum = 0

for i, name in enumerate(allNames):
  sum += (nameValue(name) * (i + 1))

print sum
