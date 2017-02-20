#!/usr/bin/python
#Find Fibonacci numbers

#init variables F1 and F2
F1 = 1
F2 = 1
Fsum = 0

#List to hold the fb (Fibonacci numbers)
fb = []
fb.append(F1)
fb.append(F2)

#For range times, find numbers.  Already seeded the list with [1,1]
for i in range(10):
    fb.append((fb[i] + fb[i+1]))

print fb
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
