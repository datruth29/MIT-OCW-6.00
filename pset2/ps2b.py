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
counter = 0


for n in range(1, limit+1):

  # If the number of consecutive numbers that solve the equation, then
  # ANY numbers afterwards will solve for it as well. As such, counter
  # keeps track of this. The statement below checks for this, and if
  # it finds it, it breaks out of the logic as it doesn't need to go
  # further.

  if counter == min(a,b,c):
    break
  for z in range(0, n/c+1):
    for y in range(0,n/b+1):
      for x in range(0, n/a+1):
        if x*a + y*b + z*c == n and n not in solutions:
          solutions += (n,)
          if max(solutions)-1 not in solutions:
            largest = max(solutions)-1
            counter = 0
          else:
            counter += 1

print solutions
print largest

