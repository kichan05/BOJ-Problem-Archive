def get_tile(x, y):
    if((x + y) % 2 == 0):
        return "#"
    else:
        return "."

M, N = map(int, input().split())
U, L, R, D = map(int, input().split())

for y in range(U):
    for x in range(L + N + R):
        print(get_tile(x, y), end = "")
    print()
    
for y in range(U, U + M):
    for x in range(L):
        print(get_tile(x, y), end = "")
    
    print(input(), end="")
    
    for x in range(L + N, L + N + R):
        print(get_tile(x, y), end = "")
        
    print()
    
for y in range(U + M, U + M + D):
    for x in range(L + N + R):
        print(get_tile(x, y), end = "")
    print()
