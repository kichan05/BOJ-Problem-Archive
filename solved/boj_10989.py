import sys

N = int(input())

nums = set()
count = {}

for _ in range(N):
    num = int(sys.stdin.readline().strip())
    nums.add(num)
    
    if(str(num) not in count):
        count[str(num)] = 0

    
    count[str(num)] += 1
    
nums = sorted(list(nums))

for num in nums:
    for _ in range(count[str(num)]):
        print(num)
