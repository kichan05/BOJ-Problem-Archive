N = int(input())

for _ in range(N):
    words = input().split()
    
    for i in words:
        print(i[::-1], end = " ")
        
    print()
