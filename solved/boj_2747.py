N = int(input())

nums = [-1 for i in range(N + 1)]

def fun(n):
    if(nums[n] != -1):
        return nums[n]
        
    if(n == 0):
        return 0
    elif(n <= 2):
        return 1
    nums[n] = fun(n - 1) + fun(n - 2)
    
    return nums[n]
    
print(fun(N))
