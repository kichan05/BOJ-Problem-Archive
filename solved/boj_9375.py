T = int(input())

for _ in range(T):
    typeCount = {}
    n = int(input())
    
    for _ in range(n):
        name, type_ = tuple(input().split())
        
        if(type_ in typeCount):
            typeCount[type_] += 1
        else:
            typeCount[type_] = 2
        
    
    result = 1
    
    for type_, i in typeCount.items():
        # print(type_, i)
        result *= i
        
    print(result - 1)
