import sys

N = int(input())
A, B = map(int, input().split())

points = set()
count = 0

for _ in range(N):
    points.add(tuple(map(int, sys.stdin.readline().strip().split())))
    
for x, y in points:
    x1, y1 = x + A, y
    x2, y2 = x, y + B
    x3, y3 = x + A, y + B
    
    res = True
    if((x1, y1) not in points):
        continue
    
    if((x2, y2) not in points):
        continue
    
    if((x3, y3) not in points):
        continue
    
    count += 1
    
print(count)
