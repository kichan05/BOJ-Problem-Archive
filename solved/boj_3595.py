V = int(input())
_V = V

minS = float('inf')

mins = []

for a in range(1, V + 1):
    if(a ** 3 > V):
        break
    
    if(V % a != 0):
        continue
    
    V //= a;
    
    for b in range(1, V + 1):
        if(V % b != 0):
            continue
            
        c = V // b
    
        S = a * b + b * c + a * c
        
        if(minS > S):
            mins = [a, b, c]
            # print(mins)
            minS = S
            
    V = _V
        
        
print(*mins)
