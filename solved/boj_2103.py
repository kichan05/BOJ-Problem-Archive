N = int(input())

xList = {}
yList = {}

for _ in range(N):
    x, y = map(int, input().split())
    
    if(str(x) not in xList):
        xList[str(x)] = []
        
    xList[str(x)].append(y)
        
    if(str(y) not in yList):
        yList[str(y)] = []
        
    yList[str(y)].append(x)

sum_ = 0
for x, ys in xList.items():
    ys.sort()
    for y in range(0, len(ys), 2):
        sum_ += ys[y + 1] - ys[y]
        
for y, xs in yList.items():
    xs.sort()
    for x in range(0, len(xs), 2):
        sum_ += xs[x + 1] - xs[x]
        
print(sum_)
