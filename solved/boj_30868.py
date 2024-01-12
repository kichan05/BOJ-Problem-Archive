T = int(input())

for _ in range(T):
    n = int(input())
    
    for _ in range(n // 5):
        print("++++", end=" ")
    
    print("|" * (n % 5))
