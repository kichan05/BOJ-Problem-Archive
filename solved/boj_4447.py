N = int(input())

for _ in range(N):
    name = input()
    
    g = 0
    b = 0
    
    for n in name.lower():
        if(n == "g"):
            g += 1
        if(n == "b"):
            b += 1
            
            
    if(g > b):
        print(f"{name} is GOOD")
    elif(g < b):
        print(f"{name} is A BADDY")
    else:
        print(f"{name} is NEUTRAL")
