N = int(input())

cow = [-1 for i in range(11)]

count = 0

for _ in range(N):
    num, location = map(int, input().split())
    
    if(cow[num] != -1 and cow[num] != location):
        count += 1
    
    cow[num] = location
        
print(count)
