N = input()

for i in range(1, len(N)):
    fitst = 1
    for j in range(0, i):
        fitst *= int(N[j])
    
    second = 1
    for j in range(i, len(N)):
        second *= int(N[j])
        
    if(fitst == second):
        print("YES")
        exit(0)
    

print("NO")
