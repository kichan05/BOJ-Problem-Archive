import sys

sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())

Y, X, d = map(int, input().split())
count = 0

grp = []
grp_ = [[0 for i in range(M)] for j in range(N)]

def getLeft():
    global X, Y, d
    
    if(d == 0 and X + 1 <= M - 2):
        return X + 1, Y
    
    if(d == 1 and Y + 1 <= N - 2):
        return X, Y + 1
        
    if(d == 2 and X - 1 >= 1):
        return X - 1, Y
        
    if(d == 3 and Y - 1 >= 1):
        return X, Y - 1
        
    return None, None
    
def getBack():
    global X, Y, d
    
    if(d == 0 and Y + 1 <= N - 2):
        return X, Y + 1
    
    if(d == 1 and X - 1 >= 1):
        return X - 1, Y
        
    if(d == 2 and Y - 1 >= 1):
        return X, Y - 1
        
    if(d == 3 and X + 1 <= M - 2):
        return X + 1, Y
        
    return None, None

def turnLeft():
    global d
    
    d += 1
    d %= 4

def isCanGo(x, y):
    if(x == None):
        return False
        
    if(grp_[y][x] == 1):
        return False
    
    if(grp[y][x] == 1):
        return False
    
    return True
    
def fun():
    global X, Y, d, count
    
    print(X, Y, d)
    
    if(grp_[Y][X] != 1):
        count += 1
    
    grp_[Y][X] = 1
    
    for i in range(4):
        _x, _y = getLeft()
        
        if(not isCanGo(_x, _y)):
            turnLeft()
            continue
        
        turnLeft()
        X, Y = _x, _y
        fun()
        return
    
    _x, _y = getBack()
    
    if(_x == None or grp[_y][_x] == 1):
        return
    
    X, Y = _x, _y
    fun()
    
    
for i in range(N):
    row = input().split()
    row = map(int, row)
    row = list(row)
    
    grp.append(row)
    

fun()

print(count)

