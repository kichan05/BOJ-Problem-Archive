n = int(input())

T = []
P = []

f = -1

for i in range(n):
    t, p = map(int, input().split())
    
    T.append(t)
    P.append(p)
    
    if(f == -1 or P[f] < p):
        f = i
        
if(P[f] == 0):
    print(0)
else:
    print(T[f] + f * 20)
