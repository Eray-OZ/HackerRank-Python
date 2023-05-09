# https://www.hackerrank.com/challenges/np-concatenate/problem



import numpy as np


a = input().strip().split(' ')

x = []
y = []


for _ in range(int(a[0])):
    aI = input().strip().split(' ')
    aI = list(map(int, aI))
    x.append(aI)

    
for _ in range(int(a[1])):
    aI = input().strip().split(' ')
    aI = list(map(int, aI))
    y.append(aI)
    

        
    
    
answer = np.concatenate((x,y))

print(answer)    
        
    
        
    
   
