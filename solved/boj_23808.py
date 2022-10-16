N = int(input())

for i in range(2 * N):
    print("@" * N, end="")
    print(" " * (N * 3), end="")
    print("@" * N)
    
for i in range(N):
    print("@" * (N * 5))
    
for i in range(N):
    print("@" * N, end="")
    print(" " * (N * 3), end="")
    print("@" * N)
    
for i in range(N):
    print("@" * (N * 5))
