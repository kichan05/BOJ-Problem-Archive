import sys
sys.setrecursionlimit(10**9)

N = int(input())

grp = []
grp_ = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    grp.append(list(input()))
    
def fun(x, y, ch):
    # 색맹이 아닐때
    if(not 0 <= x <= N -1 or not 0 <= y <= N - 1):
        return
    
    if(grp_[y][x] == 1 or grp[y][x] != ch):
        return
    
    grp_[y][x] = 1
    
    fun(x - 1, y, ch)
    fun(x + 1, y, ch)
    fun(x, y - 1, ch)
    fun(x, y + 1, ch)
    
def fun_(x, y, ch):
    # print(x, y, ch, grp[y][x], end=" - ")
    
    # 색맹이 일때
    if(not (0 <= x <= N - 1 and 0 <= y <= N - 1)):
        # print("범위 X")
        return
    
    if(grp_[y][x] == 1):
        return
    
    if(ch == "B" and grp[y][x] != "B"):
        # print("다름")
        return
    
    if(ch != "B" and grp[y][x] == "B"):
        # print("다름")
        return
    
    # print("함")
    
    grp_[y][x] = 1
    
    fun_(x - 1, y, ch)
    fun_(x + 1, y, ch)
    fun_(x, y - 1, ch)
    fun_(x, y + 1, ch)
    
count = 0 #색맹이 아닐때
count_ = 0 #색맹일때

# print("색맹 X")
    
for y in range(N):
    for x in range(N):
        if(grp_[y][x] != 1):
            fun(x, y, grp[y][x])
            count += 1

# print("색맹")

grp_ = [[0 for i in range(N)] for j in range(N)]

for y in range(N):
    for x in range(N):
        if(grp_[y][x] != 1):
            fun_(x, y, grp[y][x])
            count_ += 1
            
print(count, count_)
