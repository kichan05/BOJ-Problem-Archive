M, N = tuple(map(int, input().split()))

sx = sy = x = y = 0
dire = 0

count = 0
fillCount = 0
maxCount = M * N

while(fillCount != maxCount):
    fillCount += 1
    
    # print(f"{x} {y}")
        
    if(dire == 0):
        x += 1
    elif(dire == 1):
        y += 1
    elif(dire == 2):
        x -= 1
    elif(dire == 3):
        y -= 1
        
    if(dire == 0 and x == N - 1 and y == sy):
        count += 1
        dire = 1
        
        sy += 1
        
    elif(dire == 1 and x == N - 1 and y == M - 1):
        count += 1
        dire = 2
        
        N -= 1
        
    elif(dire == 2 and x == sx and y == M - 1):
        count += 1
        dire = 3
        
        M -= 1
        
    elif(dire == 3 and x == sx and y == sy):
        count += 1
        dire = 0
        
        sx += 1
        
print(count - 1)
