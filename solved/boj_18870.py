N = int(input())
nums = list(map(int, input().split()))


numsSort = sorted(list(set(nums)))

counts = {}

for i in range(len(numsSort)):
    counts[str(numsSort[i])] = i

for i in nums:
    print(counts[str(i)], end = " ")
