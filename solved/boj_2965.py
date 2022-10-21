N = int(input())
nums = list(map(int, input().split()))

count = 0

for i in range(2, N):
    a = nums[i] - nums[i - 1]
    b = nums[i - 1] - nums[i - 2]
    
    
    if(a * b <= 0):
        count += 1
    
if(count < 2):
    print("YES")
else:
    print("NO")
