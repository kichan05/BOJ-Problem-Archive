while(1):
    count = 0
    str_ = input()
    
    if(str_ == "#"):
        break;
        
    for i in str_:
        if(i in "aeiouAEIOU"):
            count += 1
            
    print(count)
