import sys
sys.setrecursionlimit(10**6)

T = int(input())

map_ = []
map__ = []

count = 0

M, N = 0, 0

def grp(x, y):
    global M, N, count
    
    if(not 0 <= x <= M - 1):
        return False
        
    if(not 0 <= y <= N - 1):
        return False
        
    if(map__[y][x] == 1 or map_[y][x] == 0):
        return False
        
    map__[y][x] = 1
    
    grp(x - 1, y)
    grp(x + 1,y)
    grp(x, y - 1)
    grp(x, y + 1)
    
        
    return True
    

for _ in range(T):
    
    M, N, K = map(int, input().split())

    map_ = [[0 for i in range(M)] for j in range(N)]
    map__ = [[0 for i in range(M)] for j in range(N)]
    
    for i in range(K):
        x, y = map(int, input().split())
        
        map_[y][x] = 1
        
        
        
    for y in range(N):
        for x in range(M):
            
            if(grp(x, y)):
                count += 1
            
    print(count)
    count = 0
