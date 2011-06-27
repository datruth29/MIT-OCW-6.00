#!/usr/bin/env python

# Problem Set 1a
# Name: Adam Collado
# Date: 6/27/2011

primeTest  = 3
primeCount = 0

while (primeCount != 1000):
  itercheck = 3
  divisable = 0
  while (itercheck < primeTest-(primeTest/2)) and (divisable < 1):
    if (primeTest%itercheck == 0):
      divisable+=1
    itercheck+=2
  if divisable < 1:
    print "%d is a prime" % (primeTest)
    primeCount+=1
  primeTest+=2

