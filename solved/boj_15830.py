import math

V, W, D = map(int, input().split())
count = 0

tw = W / V

while(True):
    S = 5 * ((tw) ** 2)
    
    if(D >= S):
        count += 1
        D -= S
        
        V *= 0.8
        tw *= 1.25
    else:
        break
    
print(count)
