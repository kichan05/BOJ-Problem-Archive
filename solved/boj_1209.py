nums = []

result = False

for i in range(9):
    n = int(input())
    
    nums.append(n)
    
sum_ = sum(nums)
    
for i in range(9):
    for j in range(i + 1, 9):
        if(sum_ - nums[i] - nums[j] == 100):
            nums.remove(nums[j])
            
            result = True
            break
        
    if(result):
        nums.remove(nums[i])
        break

nums.sort()

for i in nums:
    print(i)
