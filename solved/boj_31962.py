N, X = map(int, input().split())

max_s = 0

for _ in range(N):
    S, T = map(int, input().split())
    
    if(S + T > X):
        continue
    
    if(max_s < S):
        max_s = S

if(max_s == 0):
    print(-1)
else:
    print(max_s)
