x1, x2 = map(int, input().split())
a, b, c, d, e = map(int, input().split())

def integral(x):
    global a, b, c, d, e

    return a / 3 * x ** 3 + (b - d) / 2 * x ** 2 + (c - e) * x

print(int(integral(x2) - integral(x1)))