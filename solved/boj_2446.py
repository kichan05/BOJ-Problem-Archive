N = int(input())


for i in range(N - 1):
    print(" " * i, end="")
    print("*" * (1 + (N - 1 - i) * 2))


for i in range(N):
    print(" " * (N - i - 1), end="")
    print("*" * (2 * i + 1))
