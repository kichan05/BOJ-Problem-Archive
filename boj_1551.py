N, K = tuple(map(int, input().split()))

nums = list(map(int, input().split(",")))

# print(nums)

for i in range(K):
    nueList = []
    # print("실행")
    for j in range(len(nums) - 1):
        nueList.append(nums[j + 1] - nums[j])
    nums = nueList[::]

#     print(nums)
    
for n, i in enumerate(nums):
    print(i, end="")
    
    if(n + 1 != len(nums)):
        print(",", end="")
