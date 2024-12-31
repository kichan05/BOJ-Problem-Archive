A, B, C = map(int, input().split())

lines = [[] for i in range(11)]

if(B == 0 and C % A == 0):
    lines[C // A] = [i for i in range(1, 11)]
else:
    for x in range(1, 11):
        if((C - A * x) % B != 0):
            continue
        
        y = (C - A * x) // B
        
        if(not 1 <= y <= 10):
            continue
        
        lines[x].append(y)
    
for line in lines[1:]:
    line.sort()
    
    if(len(line) == 0):
        print(0)
    else: 
        print(*line)
