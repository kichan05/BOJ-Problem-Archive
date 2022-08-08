import sys
sys.setrecursionlimit(10 ** 6)

N, M, K = map(int, input().split())

grp = [[0 for i in range(M)] for j in range(N)]
grp_ = [[0 for i in range(M)] for j in range(N)]

stCount = 0
mxCount = 0

for i in range(K):
    r, c = map(int, input().split())
    
    grp[r - 1][c - 1] = 1
    

def fun(r, c):
    global stCount
    # print(r, c, end=" : ")
    
    if(grp[r][c] == 0):
        # print("방문 안함")
        return
    
    if(grp_[r][c] == 1):
        # print("방문 안함")
        return
    
    # print("방문 함")
    
    grp_[r][c] = 1
    stCount += 1
    
    if(r - 1 >= 0):
        fun(r - 1, c)
    
    if(r + 1 <= N - 1):
        fun(r + 1, c)
        
    if(c - 1 >= 0):
        fun(r, c - 1)
    
    if(c + 1 <= M - 1):
        fun(r, c + 1)
        
        
for i in range(N):
    for j in range(M):
        if(grp_[i][j] == 0 and grp[i][j] == 1):
            stCount = 0
            fun(i, j)
            
            mxCount = max(mxCount, stCount)
            
print(mxCount) 
