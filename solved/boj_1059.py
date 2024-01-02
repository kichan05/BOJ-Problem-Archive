L = int(input())
S = list(map(int, input().split()))
n = int(input())

if(n in S):
    print(0)
    exit(0)

right, left = max(S), min(S)

for i in S:
    if(i < n):
        left = max(left, i)
    if(i > n):
        right = min(right, i)
        
if(n < left):
    left = 0

print((n - left) * (right - n) - 1)