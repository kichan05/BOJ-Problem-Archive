num = list(map(int, input().split()))

A, B = min(num), max(num)

end = B * (B + 1) // 2
start = (A - 1) * A // 2

print(end - start)

