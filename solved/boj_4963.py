import sys

sys.setrecursionlimit(10 ** 6)

def fun(x, y):
#     print("방문", x, y)
    grp_[y][x] = 1
    for i in range(max(0, x - 1), min(x + 2, w)):
        for j in range(max(0, y - 1), min(y + 2, h)):
#             print("갈까", i, j, end=" --- ")

            if(i == x and j == y):
#                 print("나임")
                # 다음으로 이동할 위치가 자기 자신인 경우
                continue
            
            if(grp_[j][i] == 1):
#                 print("갔다옴")
                # 다음으로 이동할 위치가 이미 방문한 경우
                continue
            
            if(grp[j][i] == 1):
#                 print("갈게")
                # 다음으로 이동할 위치가 섬인 경우
                fun(i, j)


grp_ = []
grp = []


while 1:
    count = 0
    w, h = map(int, input().split())
    
    if(w == 0 and h == 0):
        break
    
    grp_ = [[0 for j in range(w)] for i in range(h)]
    grp.clear()
    
    for i in range(h):
        grp.append( list( map(int, input().split()) ) )
        
#     print(grp)
#     print(grp_)
    
    for i in range(w):
        for j in range(h):
            if(grp_[j][i] == 0 and grp[j][i] == 1):
                fun(i, j)
                count += 1
                
    print(count)

