R, C = map(int, input().split())

grp = []
grp_ = [[0 for i in range(C)] for j in range(R)]

stop = False

for i in range(R):
    row = list(input())
    grp.append(row) 

def fun(x, y):
    global stop
    
    if(grp[y][x] == "X" or grp_[y][x] == 1 or stop):
        return
    
    grp_[y][x] = 1
    
    count = 0
    if(x - 1 >= 0 and grp[y][x - 1] == "."):
        count += 1
    if(x + 1 <= C - 1 and grp[y][x + 1] == "."):
        count += 1
    if(y - 1 >= 0 and grp[y - 1][x] == "."):
        count += 1
    if(y + 1 <= R - 1 and grp[y + 1][x] == "."):
        count += 1
        
    if(count < 2):
        stop = True
        return
    
    if(x - 1 >= 0):
        fun(x - 1, y)
    
    if(x + 1 <= C - 1):
        fun(x + 1, y)
        
    if(y - 1 >= 0):
        fun(x, y - 1)
        
    if(y + 1 <= R - 1):
        fun(x, y + 1)
        
for y in range(R):
    for x in range(C):
        if(grp[y][x] != "X" and grp_[y][x] == 0):
            fun(x, y)
        
        if(stop):
            break
        
    if(stop):
        break
            

print(int(stop))
