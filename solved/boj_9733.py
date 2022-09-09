count = {}

totalCount = 0

while(1):
    try:
        cmd = input().split()
        
        if(cmd == None):
            break
        
        for i in cmd:
            totalCount += 1
            
            if(i in count):
                count[i] += 1
            else:
                count[i] = 1
        
        
    except EOFError:
        break

for i in ["Re", "Pt", "Cc", "Ea", "Tb", "Cm", "Ex"]:
    if(i in count):
        print(f"{i} {count[i]} {round(count[i] / totalCount, 2)}")
    else:
        print(f"{i} 0 0.00")
    
print(f"Total {totalCount} 1.00")
