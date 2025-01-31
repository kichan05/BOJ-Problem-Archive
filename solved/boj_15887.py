N = int(input())
nums = list(map(int, input().split()))

o = []

for i in range(N):
    for j in range(0, N - 1 - i):
        if(nums[j] > nums[j + 1]):
            o.append([j + 1, j + 2])
            temp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = temp
            
            
print(len(o))
for i in o:
    print(*i)
