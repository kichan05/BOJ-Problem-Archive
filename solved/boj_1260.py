import sys

sys.setrecursionlimit(10**6)
N, M, V = map(int, input().split())

grp = {}

for i in range(M):
    a, b = map(int, input().split())
    
    if(str(a) in grp):
        grp[str(a)].append(b)
    else:
        grp[str(a)] = [b]
        
    if(str(b) in grp):
        grp[str(b)].append(a)
    else:
        grp[str(b)] = [a]
        
        
        
for i in range(1, N + 1):
    if(str(i) in grp):
        grp[str(i)].sort()
    else:
        grp[str(i)] = []


bfs = []
dfs = []

bfs_ = [0 for i in range(N + 1)]
dfs_ = [0 for i in range(N + 1)]

def dfsFun(n):
    dfs_[n] = 1
    
    print(n, end = " ")
    
    dfs.extend(grp[str(n)][::-1])
    
    while len(dfs) != 0:
        next_ = dfs.pop(-1)
        if dfs_[ next_ ] == 0:
            dfsFun( next_ )
            break
        
        
def bfsFun(n):
    bfs_[n] = 1
    
    print(n, end = " ")
    
    bfs.extend(grp[str(n)])
    
    while len(bfs) != 0:
        next_ = bfs.pop(0)
        if bfs_[ next_ ] == 0:
            bfsFun( next_ )
            break
        
dfsFun(V)
print()
bfsFun(V)
