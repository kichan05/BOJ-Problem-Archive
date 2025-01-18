N = int(input())
nums = [-1] * (N + 1)

nums[1] = 0

for i in range(2, N + 1):
    nums[i] = nums[i - 1] + 1
    
    if(i % 2 == 0 and nums[i] > nums[i // 2] + 1):
        nums[i] = nums[i // 2] + 1
    
    if(i % 3 == 0 and nums[i] > nums[i // 3] + 1):
        nums[i] = nums[i // 3] + 1
        
        
print(nums[N])
