A = list(map(int, input().split()))
C = list(map(int, input().split()))

x = C[0] - A[2]
y = C[1] // A[1]
z = C[2] - A[0]

print(x, y, z)
