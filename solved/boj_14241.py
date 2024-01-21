N = int(input())
nums = list(map(int, input().split()))
nums.sort()

# print(nums)

score = 0
while len(nums) > 1:
    score += nums[-1] * nums[-2]
    new = nums[-1] + nums[-2]
    
    del nums[-1]
    del nums[-1]
    
    nums.append(new)
    
print(score)
