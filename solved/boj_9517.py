K = int(input())
N = int(input())

time = 0

for _ in range(N):
    T, Z = tuple(input().split())
    
    time += int(T)
    
    if(time >= 60 * 3 + 30):
        print(K)
        break
    
    if(Z == "T"):
        K += 1
        
        if(K == 9):
            K -= 8
