N, K = map(int, input().split())

nums = []

for _ in range(N):
    n = int(input())
    nums.append(n)
    
nums.sort()

i = 1
target = nums[0]

while(i < N):
    if(i * (nums[i] - target) <= K):
        K -= i * (nums[i] - target)
        target = nums[i]
        i += 1
    else:
        break


target += K // i
print(target)
