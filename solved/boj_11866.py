N, K = map(int, input().split())

nums = [i for i in range(1, N + 1)]
result = []

idx = K - 1

while(len(nums) > 0):
    idx %= len(nums)
    
    result.append(nums.pop(idx))
    
    idx += K - 1
    
    
print("<", end="")

for n, i in enumerate(result):
    print(i, end="")
    
    if(n != N - 1):
        print(", ", end="")
    else:
        print(">")
