def isD():
    d = A[1] - A[0]
    for i in range(2, N):
        if(d != A[i] - A[i - 1]):
            return False
        
    return True
    
N = int(input())

A = list(map(int, input().split()))

if(N == 1):
    print("YES")
    print(0)
    print(A[0])
    exit(0)
    

result = isD()
if(result):
    print("YES")
    d = A[1] - A[0]
    # B = [d * i for i in range(5)]
    # C = [d * i + A[0] - d for i in range(5)]
    
    print(*A)
    print(*([0] * N))
    
    
else:
    print("NO")
