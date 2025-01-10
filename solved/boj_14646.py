N = int(input())
nums = list(map(int, input().split()))

st = [0] * (N + 1)

count = 0
max_count = 0

for n in nums:
    if(st[n]):
        count -= 1
    else:
        st[n] = 1
        count += 1
        
    max_count = max(max_count, count)
    
print(max_count)
