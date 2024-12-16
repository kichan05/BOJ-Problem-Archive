N = int(input())
X, S = map(int, input().split())

flag = True

for _ in range(N):
    c, p = map(int, input().split())
    
    if(X >= c and S < p):
        print("YES")
        flag = False
        break;
        
if(flag):
    print("NO")
