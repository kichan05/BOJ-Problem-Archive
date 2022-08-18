while(1):
    A, B, C = map(int, input().split())
    
    if(A == 0):
        break;
        
        
    if(A ** 2 + B ** 2 == C ** 2):
        print("right")
        continue
    
    if(B ** 2 + C ** 2 == A ** 2):
        print("right")
        continue
    
    if(A ** 2 + C ** 2 == B ** 2):
        print("right")
        continue
    
    print("wrong")
    
