import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

out = []
pre = []

for i in range(n - 1):
    out.append(nums[i] > nums[i + 1])
    
    if(i == 0):
        pre.append(int(out[-1]))
    else:
        pre.append(pre[i - 1] + int(out[-1]))
    
if(n == 1):
    pass
else:
    out.append(False)
    pre.append(pre[-1])

Q = int(input())

for _ in range(Q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    
    if(n == 1):
        print(0)
        continue
    
    if(x == 0):
        sum_ = pre[y]
        
    else:
        sum_ = pre[y] - pre[x - 1]
    
    if(out[y]):
        sum_ -= 1
        
    print(sum_)
