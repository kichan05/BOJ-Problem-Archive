t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    
    print((nums[-1] - nums[0]) * 2)
