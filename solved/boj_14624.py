n = int(input())

if(n % 2 == 0):
    print("I LOVE CBNU")
    
    exit(0)
    
print("*" * n)

for i in range(n // 2 + 1):
    print(" " * int(n // 2 - i), end="")
    print("*", end="")
    
    if(i != 0):
        print(" " * (2 * i - 1), end="")
        print("*", end="")
    
    
    print()
