N = int(input())
nums = input().split()
nums = map(int, nums)
nums = list(nums)


count = {}

for i in nums:
    if(str(i) in count):
        count[str(i)] += 1
    else:
        count[str(i)] = 1


M = int(input())
findNums = input().split()
findNums = map(int, findNums)
findNums = list(findNums)

for i in findNums:
    if(str(i) in count):
        print(count[str(i)], end=" ")
    else:
        print(0, end=" ")
