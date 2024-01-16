N = int(input())

for _ in range(N):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    
    if(x1 == x2 and x3 == x4):
        if(x1 == x3):
            print("LINE")
        else:
            print("NONE")
    
        continue
    
    if(x1 == x2):
        a2 = (y3 - y4) / (x3 - x4)
        b2 = y3 - a2 * x3
        x = x1
        y = a2 * x + b2
        print("POINT %.2f %.2f" %(x, y))
        continue
    
    if(x3 == x4):
        a1 = (y1 - y2) / (x1 - x2)
        b1 = y1 - a1 * x1
        x = x3
        y = a1 * x + b1
        print("POINT %.2f %.2f" %(x, y))
        continue
    
    a1 = (y1 - y2) / (x1 - x2)
    a2 = (y3 - y4) / (x3 - x4)
    
    b1 = y1 - a1 * x1
    b2 = y3 - a2 * x3
    
    if(a1 == a2):
        if(b1 == b2):
            print("LINE")
        else:
            print("NONE")
            
    else:
        x = (-b1 + b2) / (a1 - a2)
        y = a1 * x + b1
        
        print("POINT %.2f %.2f" %(x, y))
