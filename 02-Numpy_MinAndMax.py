import numpy as np

dim = input().strip().split(' ')
arr = []

for _ in range(int(dim[0])):
    ip = input().strip().split(' ')
    ip = list(map(int, ip))
    arr.append(ip)
    
arr = np.array(arr)    

min = np.min(arr, axis = 1)

print(max(min))
