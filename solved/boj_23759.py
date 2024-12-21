N = int(input())

current = int(input())

sum_ = 0

for _ in range(N):
    target = int(input())
    
    left = target - current
    
    if(left < 0):
        left += 360
        
    right = 360 - left
    
    a = min(left, right)
    
    sum_ += a
    
    current = target
    
print(sum_)
