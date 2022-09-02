T = int(input())


for _ in range(T):
    result = True
    str_ = input()
    
    stk = []
    count = 0
    
    for i in str_:
        if(i == ")"):
            if(count == 0):
                result = False
                break
            
            count -= 1
                
        else:
            count += 1
            
            
    if(count != 0):
        result = False
        
    if(result):
        print("YES")
    else:
        print("NO")
