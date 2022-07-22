while 1:
    R, C = map(int, input().split())
    
    if(R == 0 and C == 0):
        break
    
    map_ = [[0 for i in range(C)] for i in range(R)]
    
    for i in range(R):
        row = input()
        for j, n in enumerate(row):
            if(n == "*"):
                map_[i][j] = "*"
                for y in range(max(0, i - 1), min(i + 1, R - 1) + 1):
                    for x in range(max(0, j - 1), min(j + 1, C - 1) + 1):
                        if(map_[y][x] != "*"):
                            map_[y][x] += 1
    
    for i in map_:
        for j in i:
            print(j, end="")
        print()
