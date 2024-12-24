N = int(input())

name = input()

l = len(name)

def fun():
    title = input()
    
    i = 1
    
    
    while(True):
        current_i_length = (i - 1) * (l - 1) + l
        if(len(title) < current_i_length):
            break
        
        for j in range(len(title) - current_i_length + 1):
            for k in range(l):
                m = i * (k + 1) + j - i
                # print(m, end=", ")
                if(title[m] != name[k]):
                    break
                
                if(k == l - 1):
                    return True
                
            
            
        i += 1
        
    return False

count = 0
for _ in range(N):
    if(fun()):
        count += 1
        
print(count)
