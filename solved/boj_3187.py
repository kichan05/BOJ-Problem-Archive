import sys
sys.setrecursionlimit(10**6)

R, C = map(int, input().split())

grp = []

grp_ = [[0 for i in range(C)] for j in range(R)]

for i in range(R):
    row = list(input())
    
    grp.append(row)
    
vC, kC = 0, 0
totalV, totalK = 0, 0
    
def fun(x, y):
    global vC, kC
    if(not(0 <= y <= R - 1 and 0 <= x <= C - 1)):
        return
    
    if(grp_[y][x] == 1 or grp[y][x] == "#"):
        return
    
    grp_[y][x] = 1
    
    if(grp[y][x] == "v"):
        vC += 1
    elif(grp[y][x] == "k"):
        kC += 1
    
    fun(x - 1, y)
    fun(x + 1, y)
    fun(x, y - 1)
    fun(x, y + 1)
    
for x in range(C):
    for y in range(R):
        if(grp_[y][x] != 1 and grp[y][x] != "#"):
            vC, kC = 0, 0
            
            fun(x, y)
            
            if(vC < kC):
                totalK += kC
            else:
                totalV += vC
                
print(totalK, totalV)
