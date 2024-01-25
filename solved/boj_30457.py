N = int(input())
nums = list(map(int, input().split()))

count = {}

for i in nums:
    if(str(i) not in count):
        count[str(i)] = 0
    
    count[str(i)] = min(count[str(i)] + 1, 2)
    
print(sum(count.values()))
