import sys
sys.setrecursionlimit(10**6)

R, C = map(int, input().split())

grp = []

grp_ = [[0 for i in range(C)] for j in range(R)]



vC = 0
oC = 0

totalVC = 0
totalOC = 0


def fun(x, y):
    global vC
    global oC
    
    if(grp_[y][x] == 1 or grp[y][x] == "#"):
        return
    
    
    grp_[y][x] = 1
    
    if(grp[y][x] == "o"):
        oC += 1
    elif(grp[y][x] == "v"):
        vC += 1
        
    
    if(x - 1 >= 0):
        fun(x - 1, y)
        
    if(x + 1 <= C - 1):
        fun(x + 1, y)
        
    if(y - 1 >= 0):
        fun(x, y - 1)
        
    if(y + 1 <= R - 1):
        fun(x, y + 1)
    

for i in range(R):
    grp.append(input())
    
# print(grp)


for y in range(R):
    for x in range(C):
        if(grp[y][x] != "#" and grp_[y][x] == 0):
            
            oC = 0
            vC = 0
            fun(x, y)
            
            # print(x, y, oC, vC)
            
            
            if(vC < oC):
                totalOC += oC
            else:
                totalVC += vC
            
print(totalOC, totalVC)
