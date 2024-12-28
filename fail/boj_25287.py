T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(lambda x : N - x + 1, A))
    
    min_ = min(A[0], B[0])
    max_ = max(A[-1], B[-1])
    
    isFlag = True
    
    for i in range(1, N // 2 + 1):
        fa = A[i]
        fb = B[i]
    
        fa_ = min_ <= fa <= max_
        fb_ = min_ <= fb <= max_
        
        if(fa_ and fb_):
            f = min(fa, fb)
        elif(fa_):
            f = fa
        elif(fb_):
            f = fb
        else:
            isFlag = False
            break
        
        min_ = f
        
        if(i == N // 2):
            break
        
        la = A[N - i]
        lb = B[N - i]
    
        la_ = min_ <= la <= max_
        lb_ = min_ <= lb <= max_
        
        if(la_ and lb_):
            l = max(la, lb)
        elif(la_):
            l = la
        elif(lb_):
            l = lb
        else:
            isFlag = False
            break
        
        
        max_ = l
        
        
    if(isFlag and min_ <= max_):
        print("YES")
    else:
        print("NO")
