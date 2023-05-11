# https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem?isFullScreen=true&h_r=next-challenge&h_v=zen


import numpy as np
np.set_printoptions(legacy="1.13")


arr = input().strip().split(' ')

arr = list(map(float, arr))

arr = np.array(arr)


print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))


