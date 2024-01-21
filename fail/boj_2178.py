import sys
input = sys.stdin.readline

N, M = map(int, input().split())
map_ = []
que = [(0, 0, 1)]

_bfs = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(N):
    row = list(map(int, list(input())))
    map_.append(row)
    
while (len(que) >= 1):
    x, y, count = que[0]
    del que[0]
    _bfs[y][x] = 1
    # print(x, y, que)
    
    
    if(y == N - 1 and x == M - 1):
        print(count)
        break
    
    next_ = [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]
    
    for nx, ny in next_:
        if(0 <= nx < M and 0 <= ny < N and _bfs[ny][nx] == 0 and map_[ny][nx] == 1):
            que.append((nx, ny, count + 1))
