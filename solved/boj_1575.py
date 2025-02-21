N, M = map(int, input().split())

map_ = []
_dfs = [[None for _ in range(N)] for _ in range(M)]

def search(r, c):
    if(r == M - 1 and c == N - 1):
        return True
        
    if(_dfs[r][c] != None):
        return _dfs[r][c]
    
    res1, res2 = False, False
    if(r + 1 <= M - 1 and map_[r + 1][c] == 1):
        res1 = search(r + 1, c)
        
    if(c + 1 <= N - 1 and map_[r][c + 1] == 1):
        res2 = search(r, c + 1)
    
    _dfs[r][c] = res1 or res2
    
    return res1 or res2

for _ in range(M):
    map_.append(list(map(int, input().split())))
    
res = search(0, 0)

if(res):
    print("Yes")
else:
    print("No")
