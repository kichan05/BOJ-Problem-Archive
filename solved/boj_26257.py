import sys

N, M, Q = map(int, input().split())
ptr = [0] * (M + 1)
object_ = [0] * (N + 1)

for p in range(1, M + 1):
    o = int(sys.stdin.readline().strip())
    
    ptr[p] = o
    object_[o] += 1
    
for _ in range(Q):
    commend = input().split()
    c = commend[0]
    x = int(commend[1])
    
    if(c == "assign"):
        y = int(commend[2])
        object_[ptr[x]] -= 1
        ptr[x] = ptr[y]
        object_[ptr[x]] += 1
        
    elif(c == "swap"):
        y = int(commend[2])
        
        temp = ptr[x]
        ptr[x] = ptr[y]
        ptr[y] = temp
        
    elif(c == "reset"):
        object_[ptr[x]] -= 1
        ptr[x] = 0
        
save = []

for i in range(1, N + 1):
    if(object_[i] != 0):
        save.append(i)
        
print(len(save))
for o in save:
    print(o)

