# https://www.hackerrank.com/challenges/np-shape-reshape/problem?isFullScreen=true


import numpy as np



arr = input().strip().split(' ')

arr = list(map(int, arr))

arr = np.array(arr)

print(arr.reshape(3,3))

