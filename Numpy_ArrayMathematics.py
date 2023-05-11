# https://www.hackerrank.com/challenges/np-array-mathematics/problem?isFullScreen=true





import numpy as np


size = input().strip().split(' ')
size = list(map(int,size))

A = []
B = []

for _ in range(size[0]):
    I = input().strip().split(' ')
    I = list(map(int,I))
    A.append(I)
    
for _ in range(size[0]):
    I = input().strip().split(' ')
    I = list(map(int,I))
    B.append(I)
    
    
print(np.add(A,B))
print(np.subtract(A,B))
print(np.multiply(A,B))
print(np.floor_divide(A,B))
print(np.mod(A,B))
print(np.power(A,B))


