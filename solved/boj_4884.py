import math

while True:
    G, T, A, D = map(int, input().split())
    
    if(G == -1):
        break
    
    l_count = G * T * (T - 1) // 2
    total_team = G * A + D
    
    l = math.log2(total_team)
    if(l != int(l)):
        l = int(l) + 1
    else:
        l = int(l)
    
    y = 2 ** l - total_team
    
    t_count = 2 ** l - 1
    
    x = l_count + t_count
    
    print(f"{G}*{A}/{T}+{D}={x}+{y}")
