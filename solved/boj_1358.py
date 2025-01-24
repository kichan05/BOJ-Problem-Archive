import math

W, H, X, Y, P = map(int, input().split())
R = H // 2

count = 0

for _ in range(P):
    x, y = map(int, input().split())
    
    if(X <= x <= X + W and Y <= y <= Y + H):
        count += 1
        continue
       
    d = math.sqrt((x - X) ** 2 + (y - (Y + R)) ** 2)
    if(d <= R):
        count += 1
        continue
        
    d = math.sqrt((X + W - x) ** 2 + (y - (Y + R)) ** 2)
    if(d <= R):
        count += 1
        continue
            
print(count)
