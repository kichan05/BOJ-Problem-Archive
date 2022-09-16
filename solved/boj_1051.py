N, M = map(int, input().split())

map_ = []

for _ in range(N):
    row = list(input())
    row = map(int, row)
    row = list(row)
    
    map_.append(row)
    
mxSize = 0

# print(map_)
    
for y in range(N):
    for x in range(M):
        current = map_[y][x]
        
        for d in range(min(M - x, N - y)):
            # print(y, x, d)
            
            if(current != map_[y][x + d]):
                # print("케이스 1 다름")
                continue
            
            if(current != map_[y + d][x]):
                # print("케이스 2 다름")
                continue
                
            if(current != map_[y + d][x + d]):
                # print("케이스 3 다름")
                continue
                
            mxSize = max(mxSize, d + 1)
            
            # print("성공", mxSize)

    
print(mxSize ** 2)
