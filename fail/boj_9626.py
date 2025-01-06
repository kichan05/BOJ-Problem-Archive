def row(is_even, col_count):
    text = ""
    
    for i in range(int(is_even), col_count + int(is_even)):
        if(i % 2 == 0):
            text += "#"
        else:
            text += "."
            
    return text

M, N = map(int, input().split())
U, L, R, D = map(int, input().split())

for i in range(U):
    print(row(i % 2, N + L + R))
    
for i in range(U, U + M):
    print(row(i % 2, L), end = "")
    print(input(), end="")
    print(row((i + N % 2) % 2, R))
    
for i in range(U + M, U + M + D):
    print(row(i % 2, N + L + R))
