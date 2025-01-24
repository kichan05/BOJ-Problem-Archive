N = int(input())

nums = [0] * (N + 1)
nums[0] = 1

for n in range(1, N + 1):
    for i in range(n):
        nums[n] += nums[i] * nums[n - i - 1]
        
# print(nums)
print(nums[N])
