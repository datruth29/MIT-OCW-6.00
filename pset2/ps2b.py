#! /usr/bin/env python

# Problem Set 2b
# Name: Adam Collado
# Date: 7/27/2011

a = input("Enter a quantity for your 1st package: ")
b = input("Enter a quantity for your 2nd package: ")
c = input("Enter a quantity for your 3rd package: ")

largest = 0
limit = 200
solutions = ()

for n in range(0, limit+1):
    for z in range(0, n/c+1):
      for y in range(0,n/b+1):
        for x in range(0, n/a+1):
          if x*a + y*b + z*c == n and n not in solutions:
            solutions += (n,)

for i in range(0, max(solutions)+1):
  if i not in solutions: largest = i

print solutions
print largest

