n = int(input())
mxIdx = 0

for i in range(n):
    Ns = list(map(int, input().split()))
    
    rand_ = {}
    
    mx = 0;
    
    for N in Ns[1:]:
        
        if(str(N) in rand_):
            rand_[str(N)] += 1;
        else:
            rand_[str(N)] = 1;
        
        if(mx < rand_[str(N)]):
            mx = rand_[str(N)]
            mxIdx = N;
    
    if(mx > Ns[0] / 2):
        print(mxIdx)
    else:
        print("SYJKGW")
