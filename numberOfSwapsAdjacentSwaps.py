#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Takes two arrays containing the same numbers in jumbled order as input and 
calculates the number os swaps needed to make both the arrays the same. The 
constraint here is that only adjacent numbers can be swapped.
"""

n = input("Enter the number of numbers: ")
n = int(n)
arr1 = list()

print("Enter the elements of array 1:")
for _ in range(n):
    arr1.append(int(input()))
    
arr2 = list()
print("Enter the elements of array 2:")
for _ in range(n):
    arr2.append(int(input()))
    
arr2Pos = dict()
for i in range(n):
    arr2Pos[arr2[i]] = i
    
for i in range(n):
    arr2[i] = arr2Pos[arr1[i]]
    
#Calculate the number of inversions in arr2
inv = 0
for i in range(n):
    for j in range(i + 1, n):
       if(arr2[i] > arr2[j]):
           inv = inv + 1

print("Number os swaps needed = ", inv)