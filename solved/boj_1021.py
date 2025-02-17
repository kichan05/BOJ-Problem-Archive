N, M = map(int, input().split())
nums = list(map(int, input().split()))

queue = list(range(1, N + 1))

count = 0

for num in nums:
    index = queue.index(num)
    
    if(index <= len(queue) // 2):
        count += index
        queue = queue[index + 1:] + queue[:index]
    else:
        count += len(queue) - index
        queue = queue[index + 1:] + queue[:index]
        
print(count)
