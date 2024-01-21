import math
f = math.factorial

n, m = map(int, input().split())

print(f(n) // (f(m) * f(n - m)))
