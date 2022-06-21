def fun(str):
    result = []
    last = ""
    st = ""
    
    for i in str:
        
        if(last == ""):
            st += i
        elif(last == i):
            st += i
        elif(last != i):
            result.append(st)
            st = i
        
        last = i
        
    result.append(st)
    
    return result

str_ = input()
str_ = fun(str_)

counts = [0, 0]

for i in str_:
    if("0" in i): counts[0] += 1
    elif("1" in i): counts[1] += 1
    
print(min(counts))
