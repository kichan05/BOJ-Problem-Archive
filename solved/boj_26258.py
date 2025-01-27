import sys

N = int(input())
nums = []

def search(key):
    left = 0
    right = N - 1
    
    while True:
        center = (left + right) // 2
        
        if(nums[center][0] <= key < nums[center + 1][0]):
            return center
            
        if(key < nums[center][0]):
            right = center
            
        elif(nums[center + 1][0] <= key):
            left = center

for _ in range(N):
    p = map(int, sys.stdin.readline().strip().split())
    nums.append(tuple(p))
    
Q = int(input())
for _ in range(Q):
    k = float(sys.stdin.readline().strip())
    position1 = search(k)
    x1, y1 = nums[position1]
    x2, y2 = nums[position1 + 1]
    
    d = (y2 - y1) / (x2 - x1)
    if(d > 0):
        print(1)
    elif(d < 0):
        print(-1)
    else:
        print(0)
    

