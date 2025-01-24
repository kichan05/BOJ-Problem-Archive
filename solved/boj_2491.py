N = int(input())
nums = list(map(int, input().split()))

max_size = 1
size = 1

for i in range(1, N):
    if(nums[i - 1] <= nums[i]):
        size += 1
    else:
        size = 1
        
    max_size = max(max_size, size)
    
size = 1
    
for i in range(1, N):
    if(nums[i - 1] >= nums[i]):
        size += 1
    else:
        size = 1
        
    max_size = max(max_size, size)
    
print(max_size)
