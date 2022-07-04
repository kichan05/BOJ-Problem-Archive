import math

N = int(input())

X = map(int, input().split())

for i in X:
    print(int(int(i ** 0.5) ** 2 == i), end=" ")
