#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
reads two arrays having the same numbers and calculates the number of swaps 
needed in the second array to make is same as the first array
"""

arr1 = list()
arr2 = list()

num = input("Enter the number of numbers: ")
print("Enter the numbers in array 1")

for i in range(int(num)):
    n = input()
    arr1.append(int(n))
    
print("Enter the numbers in array 2")

for i in range(int(num)):
    n = input()
    arr2.append(int(n))
    
bPos = dict()
n = int(num)
    
for i in range(n):
    bPos[arr2[i]] = i
    
for i in range(n):
    arr2[i] = bPos[arr1[i]]

#Now calculate the number of swaps needed to sort arr2
count = 0
arr_dict = dict()

for index, element in enumerate(arr2):
    arr_dict[element] = index 

visited = [False] * n

for element, index in sorted(arr_dict.items()):
    if visited[element] or element == index:
        continue
    
    cycle_count = 0;
    i = element
    
    while not visited[i]:
        visited[i] = True
        
        i = arr_dict[i]
        cycle_count += 1
        
    count += cycle_count - 1
    
print("Number of swaps = ", count)