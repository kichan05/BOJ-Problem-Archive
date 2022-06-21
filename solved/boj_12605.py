N = int(input())

for i in range(N):
    print(f"Case {i + 1}: {' '.join(input().split()[::-1])}")
