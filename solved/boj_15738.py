import sys

N, K, M = map(int, input().split())
nums = list(map(int, input().split()))

for _ in range(M):
    i = int(sys.stdin.readline().strip())
    
    if(i > 0):
        if(i < K):
            continue
        
        K = i + 1 - K
    else:
        if(K < N + i + 1):
            continue
        
        K = 2 * N + i + 1 - K
        
        
    # print(K, end=", ")
print(K)
