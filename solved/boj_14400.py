import sys

n = int(input())

points_x = []
points_y = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    points_x.append(x)
    points_y.append(y)

points_x.sort()
points_y.sort()

res = 0
for i in range(n // 2):
    res += abs(points_x[i] - points_x[n - i - 1])
    res += abs(points_y[i] - points_y[n - i - 1])
    
print(res)
