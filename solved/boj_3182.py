N = int(input())

friend = [-1]
max_count = 0
max_index = 0

is_view = [False for i in range(N + 1)]

def search(num, count):
    global is_view
    
    is_view[num] = True
    
    if(not is_view[friend[num]]):
        return search(friend[num], count + 1)
        
    return count

for _ in range(N):
    friend.append(int(input()))

for i in range(1, N + 1):
    is_view = [False for i in range(N + 1)]
    
    c = search(i, 1)
    # print(i, c)
    if(max_count < c):
        max_count = c
        max_index = i
        
print(max_index)



