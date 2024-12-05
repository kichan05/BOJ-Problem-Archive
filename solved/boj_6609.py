while(True):
    try:
        M, P, L, E, R, S, N = map(int, input().split())
    except:
        break
    
    for i in range(N):
        _M = M
        M = P // S
        P = L // R
        L = _M * E
        
        
    print(M)
