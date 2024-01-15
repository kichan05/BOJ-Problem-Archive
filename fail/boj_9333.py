T = int(input())

for _ in range(T):
    R, B, M = map(float, input().split())
    
    B = int(B * 100)
    M = int(M * 100)
    
    i = 0
    while True:
        i += 1
        
        B = round(B * (100.0 + R) / 100, 2)
        B -= M
        
        if(B <= 0):
            print(i)
            break
        
        if(i > 1200):
            print("impossible")
            break
