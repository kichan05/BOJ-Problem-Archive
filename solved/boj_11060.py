N = int(input())

nums = list(map(int, input().split()))
count = [N] * N

count[0] = 0
queue = [0]

def bfs(x):
    while(queue):
        current_x = queue[0]
        del queue[0]
        
        if(current_x == N - 1):
            return count[current_x]
            
        for next_x in range(current_x + 1, current_x + nums[current_x] + 1):
            if(next_x < N and count[current_x] + 1 < count[next_x]):
                queue.append(next_x)
                count[next_x] = count[current_x] + 1
                
        
    return -1
    
print(bfs(0))
