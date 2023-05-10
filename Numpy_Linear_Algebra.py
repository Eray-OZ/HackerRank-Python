# https://www.hackerrank.com/challenges/np-linear-algebra/problem?isFullScreen=true


import numpy as np
from numpy import linalg


N = int(input())

arr = []

for _ in range(N):
    I = input().strip().split(' ')
    I = list(map(float, I))
    arr.append(I)
    
arr = np.array(arr)

print(round(linalg.det(arr),2))




