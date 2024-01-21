N, M = map(int, input().split())
map_ = []

_bfs = [[0 for _ in range(M)] for _ in range(N)]

def dfs(x, y, count):
    _bfs[y][x] = 1
    
    # print(x, y)
    
    if(y == N - 1 and x == M - 1):
        return count
        
    next_ = [(x, y - 1), (x - 1, y), (x, y + 1), (x + 1, y)]
    
    min_count = None
    
    for nx, ny in next_:
        if(0 <= nx < M and 0 <= ny < N and _bfs[ny][nx] == 0 and map_[ny][nx] == 1):
            res = dfs(nx, ny, count + 1)
            
            if(res != None):
                if(min_count == None):
                    min_count = res
                
                else:
                    min_count = min(min_count, res)
                
    return min_count
    

for _ in range(N):
    row = list(map(int, list(input())))
    map_.append(row)
    
print(dfs(0, 0, 1))
