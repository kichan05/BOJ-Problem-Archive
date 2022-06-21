N = int(input())

q = [];

for i in range(1, N + 1):
    q.append(i)
    
# print(q)

while(1):
    print(q[0], end=" ")
    del q[0]
    
    if(len(q) == 0):
        break
    
    q.append(q[0])
    del q[0]
