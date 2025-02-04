T = int(input())
ns = []

for _ in range(T):
    ns.append(int(input()))

nums = [0]

for i in range(1, max(ns) + 1):
    if(i <= 3):
        count = 1
    else:
        count = 0
        
    for j in range(1, min(4, i)):
        count += nums[i - j]
        
        
    nums.append(count)
    
# print(nums)
for n in ns:
    print(nums[n])
