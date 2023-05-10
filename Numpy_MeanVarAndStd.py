# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem?isFullScreen=true



import numpy as np


size = input().strip().split(' ')
size = list(map(int,size))

arr = []

for _ in range(size[0]):
    I = input().strip().split(' ')
    I = list(map(int,I))
    arr.append(I)
    
arr = np.array(arr)



print(np.mean(arr, axis=1))

print(np.var(arr, axis=0))

print(round(np.std(arr, axis=None),11))

