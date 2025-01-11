T = int(input())

for i in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    
    current_idx = 0
    
    print(f"Case #{i + 1}: ", end="")
    
    while(len(nums) != N):
        current_price = nums[current_idx]
        default_price = current_price * 4 // 3
        
        if(default_price in nums):
            nums.remove(default_price)
            
            current_idx += 1
            
            # print(current_price, default_price, end = "\n")
            # print(nums)
    print(*nums)
