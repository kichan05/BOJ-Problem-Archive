N = int(input())

def starPrint():
    print("* " * (N // 2 + N % 2))
    print(" *" * (N // 2))

for i in range(N):
    starPrint()
