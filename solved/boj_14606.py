N = int(input())

nums = [N]
sum_ = 0

while len(nums) != 0:
    if(nums[0] == 1):
        pass
        
    else:
        a = (nums[0] // 2)
        b = (nums[0] - nums[0] // 2)
        sum_ += a * b
        nums.extend([a, b])
    
    
    del nums[0]
    
print(sum_)