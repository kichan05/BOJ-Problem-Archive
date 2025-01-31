N = int(input())
nums = []
use_num = [False] * (1_000_001)

for _ in range(N):
    n = int(input())
    use_num[n] = True
    nums.append(n)
    
max_count = 0

for n, is_use in enumerate(use_num):
    if(not is_use):
        continue
    
    i = 0
    while nums[i] == n:
        i += 1
        if(i == N):
            break
        
    if(i == N):
        break
        
    count = 1
    pre_num = nums[i]
    
    for j in range(i + 1, N):
        if(nums[j] == n):
            continue
        
        if(pre_num != nums[j]):
            max_count = max(max_count, count)
            pre_num = nums[j]
            count = 1
            continue
        
        count += 1
        max_count = max(max_count, count)
print(max_count)
