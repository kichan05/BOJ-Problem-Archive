import sys
sys.setrecursionlimit(1500)

N = int(input())

r1, c1, r2, c2 = map(int, input().split())

_bfs = [[-1 for _ in range(N)] for _ in range(N)]

def bfs(r, c):
    bfs_queue = [(r, c)]
    _bfs[r][c] = 0
    
    while bfs_queue:
        tr, tc = bfs_queue[0]
        del bfs_queue[0]
        
        if(tr == r2 and tc == c2):
            return _bfs[tr][tc]
            
        for nr, nc in [(tr-2, tc-1), (tr-2, tc+1), (tr, tc-2), (tr, tc+2), (tr+2, tc-1), (tr+2, tc+1)]:
            # print("next", nr, nc, end="는 ")
            if(not(0 <= nr < N and 0 <= nc < N)):
                # print("범위밖이라 안함")
                pass
            elif (_bfs[nr][nc] != -1):
                pass
                # print("이미 있어서 안함", _bfs[nr][nc])
            else:
                # print("이동함")
                bfs_queue.append((nr, nc))
                _bfs[nr][nc] = _bfs[tr][tc] + 1
                
        
    return -1
    
print(bfs(r1, c1))
