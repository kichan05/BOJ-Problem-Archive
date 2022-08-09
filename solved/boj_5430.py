T = int(input())

for _ in range(T):
    reversed_ = False
    isEr = False
    
    cmd = input()
    numCount = int(input())
    
    list_ = input()
    if(list_ == "[]"):
        list_ = []
    else:
        list_ = list(list_[1 : -1].split(","))
    
    for n, i in enumerate(cmd):
        if(i == "R"):
            reversed_ = not reversed_
        
        if(i == "D"):
            if(len(list_) == 0):
                print("error")
                isEr = True
                break;
                
            if(reversed_):
                del list_[-1]
            else:
                del list_[0]
    
    if(not isEr):
        if(reversed_):
            list_ = list_[::-1]
            
        print(f'[{",".join(list_)}]')
