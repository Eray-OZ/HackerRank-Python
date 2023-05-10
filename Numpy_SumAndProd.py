# https://www.hackerrank.com/challenges/np-sum-and-prod/problem



import numpy as np

dim = input().strip().split(' ')
arr = []

for _ in range(int(dim[0])):
    I = input().strip().split(' ')
    I = list(map(int, I))
    arr.append(I)

sum = np.sum(arr, axis=0)

result = np.prod(sum)

print(result)
    



