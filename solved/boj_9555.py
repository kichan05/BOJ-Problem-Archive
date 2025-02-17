T = int(input())

school = [False for _ in range(101)]

def search(row, col):
    global school
    for r in range(max(row - 1, 0), min(row + 1, N - 1) + 1):
        for c in range(max(col - 1, 0), min(col + 1, M - 1) + 1):
            if(r == row and c == col):
                continue
            
            # print(row, col, r, c)
            if(sits[r][c] == sits[row][col]):
                school[sits[row][col]] = True
                
                return True
    # print()
    return False

for t in range(T):
    count = 0
    N, M = map(int, input().split())
    school = [False for _ in range(101)]
    
    sits = []
    
    for _ in range(N):
        sits.append(list(map(int, input().split())))
        
    for row in range(N):
        for col in range(M):
            if(school[sits[row][col]]):
                continue
            
            if(sits[row][col] == -1):
                continue
            
            count += int(search(row, col))
            
    print(count)

