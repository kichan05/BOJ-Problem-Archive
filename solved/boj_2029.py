map_ = []

for _ in range(10):
    map_.append(list(input()))
    
stick_count = 0
square_count = 0

def is_horirontal_stick(x, y):
    global map_
    
    stick = list("+--")
    
    if(x + 3 > 10):
        raise Exception("X범위 에러") 
    
    for dx in range(3):
        if(map_[y][x + dx] != stick[dx]):
            return False
            
    return True

def is_vertical_stick(x, y):
    global map_
    
    stick = list("+||")
    
    if(y + 3 > 10):
        raise Exception("y범위 에러")
    
    for dy in range(3):
        if(map_[y + dy][x] != stick[dy]):
            return False
            
    return True

def is_square(x, y, size):
    if(x + size * 3 > 10):
        raise Exception("X범위 에러")
    if(y + size * 3 > 10):
        raise Exception("y범위 에러")
        
    for i in range(y, y + 3 * size, 3):
        if(not is_vertical_stick(x, i)):
            return False
        
        if(not is_vertical_stick(x + 3 * size, i)):
            return False
            
    for j in range(x, x + 3 * size, 3):
        if(not is_horirontal_stick(j, y)):
            return False
                
        if(not is_horirontal_stick(j, y + 3 * size)):
            return False

    return True
    
for i in range(0, 11, 3):
    for j in range(0, 10, 3):
        if(j != 9 and is_horirontal_stick(j, i)):
            stick_count += 1
            
        if(i != 9 and is_vertical_stick(j, i)):
            stick_count += 1
        
        for k in range(1, 4):
            if(i + 3 * k >= 10):
                continue
            if(j + 3 * k >= 10):
                continue
            
            # print(j, i, k, "사각형 검사")
            
            if(is_square(j, i, k)):
                # print("맞음")
                square_count += 1
            else:
                pass
                # print("아님")
    
A = 24 - stick_count
B = square_count

# print(square_count)

print(A, B)
