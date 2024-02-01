import sys
sys.setrecursionlimit(1500)

N, M = map(int, input().split())

def move():
    global x, y, rotate
    
    if(rotate == 0):
        nx = x + 1
        ny = y
    elif(rotate == 1):
        nx = x
        ny = y - 1
    elif(rotate == 2):
        nx = x - 1
        ny = y
    elif(rotate == 3):
        nx = x
        ny = y + 1
        
    if(not(0 <= nx <= N - 1 and 0 <= ny <= M - 1)):
        rotate += 1
        rotate %= 4
        
        return move()
        
    if(map_[ny][nx] == 1):
        rotate += 1
        rotate %= 4
        
        return move()
        
    return nx, ny

map_ = [[0 for _ in range(N)] for _ in range(M)]

x, y = 0, M - 1
rotate = 0

for i in range(N * M):
    map_[y][x] = 1
    # print(i, x, y)
    
    if(i == M * N - 1):
        break
    x, y = move()

print(x, M - 1 - y)
