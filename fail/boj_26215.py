N = int(input())

nums = list(map(int, input().split()))
nums.sort()
nums = nums[::-1]

count = 0

if(N == 1):
    if(nums[0] > 1440):
        print(-1)
    else:
        print(nums[0])
    exit(0)


while True:
    nums[0] -= 1
    if(nums[1] != 0):
        nums[1] -= 1
    
    nums.sort()
    nums = nums[::-1]
    
    count += 1
    
    if(count > 1440):
        if(nums[0] != 0):
            print(-1)
            exit(0)
            
    if(nums[0] == 0):
        break
    
print(count)
