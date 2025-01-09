N = int(input())
nums = list(map(int, input().split()))

max_ = nums[-1]
answer = 0

for i in range(N - 1, -1, -1):
    max_ = max(max_, nums[i])
    answer = max(answer, max_ - nums[i])
    
print(answer)
