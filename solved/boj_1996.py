N = int(input())

map_ = []
result = []

for i in range(N):
    map_.append(input())
    result.append([0 for j in range(N)])
    
# print(result)
    
for i in range(N):
    for j in range(N):
        if(map_[i][j] != "."):
            print("*", end="")
            continue
        
        xSt = j - 1;
        if(xSt < 0): xSt = 0
        
        xEd = j + 1;
        if(N - 1 < xEd): xEd = N - 1
        
        ySt = i - 1;
        if(ySt < 0): ySt = 0
        
        yEd = i + 1;
        if(N - 1 < yEd): yEd = N - 1
        
        
        sum = 0
        for x in range(xSt, xEd + 1):
            for y in range(ySt, yEd + 1):
                if(map_[y][x] != "."):
                    sum += int(map_[y][x])
                    
        #result[i][j] = sum
        
        if(sum < 10): print(sum, end="")
        else: print("M", end="")
        
    print()
