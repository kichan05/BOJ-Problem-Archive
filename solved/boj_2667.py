n = int(input())

grp = []
grp_ = [[0 for i in range(n)] for j in range(n)]

counts = []

for i in range(n):
    grp.append(list(map(int, input())))
    
def fun(x, y):
    if(grp_[y][x] == 1 or grp[y][x] == 0):
        return
    
    # print(x, y)
    
    grp_[y][x] = 1
    
    counts[-1] += 1

    if(x - 1 >= 0):
        fun(x - 1, y)
        
    if(x + 1 <= n - 1):
        fun(x + 1, y)
        
    if(y - 1 >= 0):
        fun(x, y - 1)
    
    if(y + 1 <= n - 1):
        fun(x, y + 1)
        


for i in range(n):
    for j in range(n):
        # print(grp_[i][j], grp[i][j], end=" : ")
        if(grp_[i][j] == 0 and grp[i][j] == 1):
            # print(i, j)
            counts.append(0)
            
            fun(j, i)
        else:
            pass
            # print("방문 ㄴ")
            
counts.sort()
print(len(counts))
for i in counts:
    print(i)
