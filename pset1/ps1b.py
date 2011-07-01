#!/usr/bin/env python

# Problem Set 1b
# Name: Adam Collado
# Date: 6/27/2011

from math import *

nTotal = int(raw_input("Please enter the number of primes you wish to calculate to : "))

# Go through a set of totals for each prime until you have the sum (logTotal)
# of the log of all found primes.
for n in range(3, nTotal):
  primeTest  = 3
  primeCount = 0
  logTotal = 0
  while(primeTest <= n):
    itercheck = 3
    divisable = 0
    while (itercheck < primeTest-(primeTest/2)) and (divisable < 1):
      if (primeTest%itercheck == 0):
        divisable+=1
      itercheck+=2
    if divisable < 1:
      primeCount+=1
      logTotal += log(primeTest)
    primeTest+=2

  ratio = float(logTotal)/float(n)
  print "Ration: %f" % (ratio)

